import React from "react";

import { BrowserRouter, Switch, Redirect, Route } from "react-router-dom";
import Main from "./components/main/Main";
import ScrollCard from "./components/hotPlace/ScrollCard";
import FeedList from "./components/feedList/FeedList";
import userInfo from "./components/user/userInfo";
import Login from "./components/user/Login";
import Register from "./components/user/Register";
import PlaceDetail from './components/placeDetail/PlaceDetail';
import Header from './components/common/Header';
import Footer from './components/common/Footer';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Route path="/feedList" component={FeedList} />
          <Route path="/spotList" component={ScrollCard} />
          <Route path="/place" component={PlaceDetail} />
          <Route path="/userinfo" component={userInfo} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/hd" component={Header} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
