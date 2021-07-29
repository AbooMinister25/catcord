function appendZero(number: number) {
  return number.toString().length === 1 ? `0${number}` : number;
}

function appendZeroThreeDigit(number: number) {
  return number.toString().length === 2 ? `0${number}` : number;
}

export default function now(): string {
  const dateTime = new Date();
  const year = dateTime.getFullYear();
  const month = appendZero(dateTime.getMonth() + 1);
  const day = appendZero(dateTime.getDate());
  const hour = appendZero(dateTime.getHours());
  const minute = appendZero(dateTime.getMinutes());
  const seconds = appendZero(dateTime.getSeconds());
  const milliseconds = appendZeroThreeDigit(dateTime.getMilliseconds());

  return `${year}-${month}-${day} ${hour}:${minute}:${seconds}.${milliseconds}`;
}