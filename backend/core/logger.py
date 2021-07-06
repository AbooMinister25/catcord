from typing import Optional
from datetime import datetime
import traceback
from sys import stdout
import os
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
    :param mode: String declaring the mode of logging used. Can be hybrid for output to stdout and file, file for output to file, or stdout to stdout.
    :param filename: Optional string declaring the filename of the log file, if logging type is hybrid or file. Do note that logs will be in the same directory as the file that calls the logging class.
    :param COLORS: Optional dictionary containing a set of ANSI escape codes to use as COLORS. Requires the following keys: end, error, info, warning and timestamp.
    """

    def __init__(
        self,
        mode: Optional[str] = "hybrid",
        filename: Optional[str] = None,
        colored: bool = True,
    ):
        invalidcount = 0
        for element in ["hybrid", "file", "stdout"]:
            if mode != element:
                invalidcount += 1
            else:
                continue
        if invalidcount == 3:
            raise AttributeError("mode must be hybrid, stdout or file.")
        self.colored = colored
        self.loggingtype = mode
        if filename:
            if not os.path.exists(f"catcord_logs/{filename}"):
                with open(f"catcord_logs/{filename}", "w") as f:
                    pass
        self.filename = f"catcord_logs/{filename}"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        if isinstance(exc_type, Exception):
            self.error(content="Exception occured while logging: ")
            self.error(content=exc_value)
        del self

    async def _log(self, logtype: str = "info", body: Optional[str] = None):
        """
        :param type: String declaring the logging type. Reccomended values are info, warning, and error.
        :param content: String containing the log content.
        """
        if self.loggingtype == "file":
            async with aiofiles.open(self.filename, mode="a+") as file:
                print(body)
                if self.colored:
                    await file.write(
                        f"{logtype} | {COLORS.get('timestamp')}{datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')}{COLORS.get('end')} | {body}\n"
                    )
                else:
                    await file.write(
                        f"{logtype} | {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')} | {body}\n"
                    )
        elif self.loggingtype == "stdout":
            if self.colored:
                stdout.write(
                    f"{logtype} | {COLORS.get('timestamp')}{datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')}{COLORS.get('end')} | {body}\n"
                )
            else:
                stdout.write(
                    f"{logtype} | {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')} | {body}\n"
                )
        else:
            if self.colored:
                async with aiofiles.open(self.filename, "a+") as file:
                    await file.write(
                        f"{logtype} | {COLORS.get('timestamp')}{datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')}{COLORS.get('end')} | {body}\n"
                    )
                stdout.write(
                    f"{logtype} | {COLORS.get('timestamp')}{datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')}{COLORS.get('end')} | {body}\n"
                )
            else:
                async with aiofiles.open(self.filename, "a+") as file:
                    await file.write(
                        f"{logtype} | {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')} | {body}\n"
                    )
                stdout.write(
                    f"{logtype} | {datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S UTC')} | {body}\n"
                )

    async def info(self, content: str = None):
        if self.colored:
            await self._log(
                logtype=f"{COLORS.get('info')}INFO{COLORS.get('end')}",
                body=f"{content}",
            )
        else:
            await self._log(logtype="INFO", body=f"{content}")

    async def warning(self, content: str = None):
        if self.colored:
            await self._log(
                logtype=f"{COLORS.get('warning')}WARNING{COLORS.get('end')}",
                body=f"{content}",
            )
        else:
            await self._log(logtype="WARNING", body=f"{content}")

    async def error(self, content: str = None, exc: Optional[bool] = False):
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

    async def debug(
        self,
        content: str = None,
    ):
        if self.colored:
            await self._log(
                logtype=f"{COLORS.get('debug')}DEBUG{COLORS.get('end')}",
                body=f"{content}",
            )
        else:
            await self._log(logtype="ERROR", body=f"{content}")

    async def success(
        self,
        content: str = None,
    ):
        if self.colored:
            await self._log(
                logtype=f"{COLORS.get('success')}SUCCESS{COLORS.get('end')}",
                body=f"{content}",
            )
        else:
            await self._log(logtype="SUCCESS", body=f"{content}")
