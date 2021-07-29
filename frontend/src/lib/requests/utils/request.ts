import axios, { AxiosRequestConfig } from "axios";
import { backendUrl } from "../../../config";
import RequestLogger from "./logger";

// A utility function for sending requests to the backend
export default function request(options: AxiosRequestConfig): void {
  axios({
    method: options.method,
    url: `${backendUrl}${options.url}`,
    data: options.data,
    headers: options.headers,
  })
    .then(() => {
      const logger = new RequestLogger();
      logger.log(options.method, options.url);
    })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.log(error);
    });
}