import React from "react";
import "./Main.scss";

import seoul from "../image/seoul_grey.png";

class Main extends React.Component {
    render() {
        return (
            <div className="main">
                <div className="circle1"></div>
                <div className="circle2"></div>
                <div className="circle3"></div>
                <div className="grid">
                    <div className="title">
                        <h1>ㅎ<br/>ㅎ<br/>ㅎ</h1>
                        <h4>핫,<br/>힙,<br/>힐링,<br/>플레이스</h4>
                        
                    </div>
                    <div className="map">
                        {/* <img className="seoul" alt="seoulMap" src={seoul}></img> */}
                    </div>
                </div>
            </div>
        );
    }
}

export default Main;
