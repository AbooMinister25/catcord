import request from "./utils/request";

export function getUser(userId: string): void {
  request({
    method: "GET",
    url: "/users",
    data: {
      id: userId
    }
  });
}
