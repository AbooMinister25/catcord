from datetime import datetime
import os
from sys import stdout
import traceback
from typing import Literal, Optional

import aiofiles

COLORS = {
    "end": "\033[0m",
    "error": "\033[31m",
    "info": "\033[32m",
    "warning": "\033[93m",
    "debug": "\033[1;33m",
    "success": "\033[1;32m",
    "timestamp": "\033[96m",
}


class Logger:
    """
    Custom logging class.

    :param mode: String declaring the mode of logging used.
    Can be hybrid for output to stdout and file, file for output to file, or stdout to stdout.
    :param filename: Optional string declaring the filename of the log file,
    if logging type is hybrid or file.
    Do note that logs will be in the same directory as the file that calls the logging class.
    :param COLORS: Optional dictionary containing a set of ANSI escape codes to use as COLORS.
    Requires the following keys: end, error, info, warning and timestamp.
    """

    def __init__(
        self,
        mode: Literal["hybrid", "file", "stdout"] = "hybrid",
        filename: Optional[str] = None,
        colored: bool = True,
    ):
        if mode not in ("hybrid", "file", "stdout"):
            raise AttributeError("mode must be hybrid, stdout or file.")

        self.colored = colored
        self.loggingtype = mode

        if filename:
            directory = f"catcord_logs/{filename}"

            if not os.path.exists(directory):
                with open(f"{directory}", "w") as f:
                    pass

        self.filename = f"catcord_logs/{filename}"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        if isinstance(exc_type, Exception):
            self.error(content="Exception occured while logging: ")
            self.error(content=exc_value)

        del self

    async def _log(self, logtype: str = "INFO", body: Optional[str] = None):
        """
        :param type: String declaring the logging type.
        Reccomended values are info, warning, and error.
        :param content: String containing the log content.
        """
        colored_log = (
            f"{logtype} | {COLORS.get('timestamp')}"
            f"{datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')}"
            f"{COLORS.get('end')} | {body}\n"
        )
        normal_log = f"{logtype} | {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')} | {body}\n"
        log = colored_log if self.colored else normal_log

        if self.loggingtype == "file":
            async with aiofiles.open(self.filename, mode="a+") as file:
                print(body)
                await file.write(log)

        elif self.loggingtype == "stdout":
            stdout.write(log)

        else:
            async with aiofiles.open(self.filename, "a+") as file:
                file.write(log)
            stdout.write(log)

    async def log(
        self,
        log_mode: Literal["info", "warning", "debug", "success"],
        content: Optional[str] = None,
    ):
        await self._log(
            logtype="{1}{0}{2}".format(
                log_mode.upper(),
                *(
                    (COLORS.get(log_mode), COLORS.get("end"))
                    if self.colored
                    else ("", "")
                ),
            ),
            body=f"{content}",
        )

    async def error_log(self, content: Optional[str] = None, exc: bool = False):
        if exc:
            if self.colored:
                content += f"\n{COLORS.get('error')}{traceback.format_exc()}"
            else:
                content += f"\n{traceback.format_exc()}"
        if self.colored:
            await self._log(
                logtype=f"{COLORS.get('error')}ERROR{COLORS.get('end')}",
                body=f"{content}",
            )
        else:
            await self._log(logtype="ERROR", body=f"{content}")
