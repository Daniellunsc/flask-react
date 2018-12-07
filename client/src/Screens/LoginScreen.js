import React from "react";
import { Redirect } from "react-router-dom";
class LoginScreen extends React.Component {
  state = {
    username: "",
    password: "",
    fireRedirect: false,
    redirectTo: ""
  };

  componentDidMount() {
    fetch("/rest", {
      method: "GET",
      credentials: "include"
    })
      .then(res => res.json())
      .then(dt => console.log(dt));
  }

  onChange = e => {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  };

  submitForm = e => {
    const { location } = this.props;
    let path  = location.state ? location.state.from.pathname : "/"
    e.preventDefault();
    fetch("/auth", {
      method: "POST",
      body: JSON.stringify(this.state),
      credentials: "include"
    })
      .then(res => res.json())
      .then(dt => {
        if (dt.status === "success") {
          this.setState({
            fireRedirect: true,
            redirectTo: path
          });
        }
      });
  };

  render() {
    const { fireRedirect, redirectTo } = this.state;
    return (
      <div className="App-centered">
        <div className="card" style={{ width: "40%" }}>
          <div className="card-header" style={{ color: "#282c34" }}>
            Login
          </div>
          <form style={{padding: 20}}>
            <div className="form-group">
              <input
                className="form-control form-control-lg"
                type="text"
                name="username"
                placeholder="Usuário"
                onChange={this.onChange}
                value={this.state.username}
              />
            </div>

            <div className="form-group ">
              <input
                className="form-control form-control-lg"
                type="password"
                name="password"
                placeholder="Senha"
                onChange={this.onChange}
                value={this.state.password}
              />
            </div>

            <input
              className="btn btn-primary btn-lg btn-block"
              type="submit"
              value="Enviar"
              onClick={this.submitForm}
            />
          </form>
          {fireRedirect && <Redirect to={redirectTo} />}
        </div>
      </div>
    );
  }
}

export default LoginScreen;
