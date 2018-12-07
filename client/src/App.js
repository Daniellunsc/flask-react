import React, { Component } from "react";
import "./App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LoginScreen from "./Screens/LoginScreen";
import ProtectedRoute from "./Components/ProtectedRoute";
import TodoList from "./Screens/TodoList";
import { CheckAuth, RefreshToken } from "./Services/AuthService";

class App extends Component {
  componentDidMount() {
    this.setRefresh();
  }

  async setRefresh() {
    let Timeout;
    let response = await CheckAuth();
    if (response.status >= 200 && response.status < 300) {
      Timeout = setInterval(function() {
        RefreshToken();
      }, 600000);
    }
  }

  render() {
    return (
      <div className="app">
        <Router>
          <Switch>
              <Route exact path="/login" component={LoginScreen} />
              <Route
                exact
                path="/protected"
                component={ProtectedRoute(TodoList)}
              />
          </Switch>
        </Router>
      </div>
    );
  }
}

export default App;
