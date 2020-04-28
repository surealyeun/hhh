import React, { Component } from "react";
import "./Follow.scss";

class Follow extends Component {
  render() {
    return (
      <div id="follow" style={{ display: "none" }}>
        <div id="follow-list">
          <div id="follow-text">
            팔로우 <div id="close-btn">X</div>
          </div>
          <ul>
            <li>
              <img
                src="https://starcitizen.tools/images/thumb/8/83/Mercury_FrontFiring_Concept.jpeg/450px-Mercury_FrontFiring_Concept.jpeg"
                alt=""
              ></img>
              <div className="id">moonyohan</div>
              <div className="follow-btn">팔로잉</div>
            </li>
            <li>
              <img
                src="https://image-notepet.akamaized.net/seimage/20170705%2F0dd120542a6004dd2a9712701c16e87e.jpg"
                alt=""
              ></img>
              <div className="id">dogdog</div>
              <div className="follow-btn">팔로잉</div>
            </li>
          </ul>
        </div>
      </div>
    );
  }
}

export default Follow;
