import chalk from "chalk";
import now from "../../utils/now";

function logMethod(method: string | undefined): string | undefined {
  switch (method) {
  case "POST":
    return chalk.hex("#91fff3")(method) + "    ";
  case "GET":
    return chalk.hex("#91a2ff")(method) + "     ";
  case "PATCH":
    return chalk.hex("#c691ff")(method) + "   ";
  case "DELETE":
    return chalk.hex("#ff91f4")(method) + "  ";
  }
}

export default class RequestLogger {
  post(url: string | undefined): void {
    console.log(`${chalk.green(now())} | ${chalk.hex("#91fff3")("POST")}     | endpoint: ${url}`);
  }

  get(url: string | undefined): void {
    console.log(`${chalk.green(now())} | ${chalk.hex("#91fff3")("GET")}      | endpoint: ${url}`);
  }

  patch(url: string | undefined): void {
    console.log(`${chalk.green(now())} | ${chalk.hex("#91fff3")("PATCH")}    | endpoint: ${url}`);
  }

  delete(url: string | undefined): void {
    console.log(`${chalk.green(now())} | ${chalk.hex("#91fff3")("DELETE")}   | endpoint: ${url}`);
  }

  log(method: string | undefined, url: string | undefined): void {
    console.log(`${chalk.green(now())} | ${logMethod(method)} | endpoint: ${url}`);
  }
}