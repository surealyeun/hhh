import React from "react";

import { BrowserRouter, Switch, Redirect, Route } from "react-router-dom";
import Main from "./components/main/Main";
import ScrollCard from "./components/hotPlace/ScrollCard2";
import FeedList from "./components/feedList/FeedList";
import userInfo from "./components/user/userInfo";
import Login from "./components/user/Login";
import Register from "./components/user/Register";
import PlaceDetail from './components/placeDetail/PlaceDetail';
import StoreDetail from './components/placeDetail/StoreDetail';
import FeedDetail from "./components/feedDetail/FeedDetail";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Route path="/feedList" component={FeedList} />
          <Route path="/feedDetail" component={FeedDetail} />
          <Route path="/spotList/:area" component={ScrollCard} />
          <Route path="/place/:id" component={PlaceDetail} />
          <Route path="/store/:id" component={StoreDetail} />
          <Route path="/userinfo" component={userInfo} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
