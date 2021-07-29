import chalk from "chalk";
import now from "./now";

function logType(type: string): string | undefined {
  switch (type.toUpperCase()) {
  case "INFO":
    return chalk.white(type) + "    ";
  case "DEBUG":
    return chalk.blue(type) + "   ";
  case "SUCCESS":
    return chalk.green(type) + " ";
  case "WARNING":
    return chalk.yellow(type) + " ";
  case "ERROR":
    return chalk.red(type) + "   ";
  case "CRITICAL":
    return chalk.white.bgRed(type);
  }
}


export default class Logger {
  info(message: string): void {
    console.log(`${chalk.green(now())} | ${chalk.white("INFO")}     | ${message}`);
  }

  debug(message: string): void {
    console.log(`${chalk.green(now())} | ${chalk.blue("DEBUG")}    | ${message}`);
  }

  success(message: string): void {
    console.log(`${chalk.green(now())} | ${chalk.green("SUCCESS")}  | ${message}`);
  }

  warning(message: string): void {
    console.log(`${chalk.green(now())} | ${chalk.yellow("WARNING")}  | ${message}`);
  }

  error(message: string): void {
    console.log(`${chalk.green(now())} | ${chalk.red("ERROR")}    | ${message}`);
  }

  critical(message: string): void {
    console.log(`${chalk.green(now())} | ${chalk.white.bgRed("CRITCAL")}  | ${message}`);
  }

  log(type: string, message: string): void {
    console.log(`${chalk.green(now())} | ${logType(type)} | ${message}`);
  }
}