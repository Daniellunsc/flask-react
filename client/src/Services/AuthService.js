export const CheckAuth = () => {
  return fetch("/checkAuth", {
    method: "GET",
    credentials: "include"
  })
};

export const RefreshToken = () => {
  return fetch("/token/refresh", {
    method: "GET",
    credentials: "include"
  })
}
