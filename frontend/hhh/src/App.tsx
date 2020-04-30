import React from "react";

import { BrowserRouter, Switch, Redirect, Route } from "react-router-dom";
import Main from "./components/main/Main";
import ScrollCard from "./components/hotPlace/ScrollCard2";
import FeedList from "./components/feedList/FeedList";
import userInfo from "./components/user/userInfo";
import Login from "./components/user/Login";
import Register from "./components/user/Register";
import PlaceDetail from "./components/placeDetail/PlaceDetail";
import StoreDetail from "./components/placeDetail/StoreDetail";
import FeedDetail from "./components/feedDetail/FeedDetail";
import mainsns from './components/main/MainSNS';
import Follow from "./components/feedList/follow/Follow";
import WritePost from "./components/Post/WritePost";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Main} />
          <Route path="/feedList" component={FeedList} />
          <Route path="/feedDetail/:id" component={FeedDetail} />
          <Route path="/spotList/:area" component={ScrollCard} />
          <Route path="/place/:id" component={PlaceDetail} />
          <Route path="/store/:id" component={StoreDetail} />
          <Route path="/userInfo" component={userInfo} />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/sns" component={mainsns} />
          <Route path="/follow" component={Follow} />
          <Route path="/writePost" component={WritePost} />
          <Redirect path="*" to="/"></Redirect>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
