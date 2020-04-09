import React from "react";
import "./Main.scss";

// import seoul from "../image/seoul_grey.png";

// var map = './mapmini.html';
// var template = {__html: __html};

class Main extends React.Component {
    render() {
        return (
            <div className="main">
                {/* <div className="circle1"></div> */}
                {/* <div className="circle2"></div>
                <div className="circle3"></div> */}
                <div className="grid">
                    <div className="title">
                        <h1>ㅎ<br/>ㅎ<br/>ㅎ</h1>
                        <h4>
                            <span id="h4-1">핫,</span><br/>
                            <span id="h4-2">힙,</span><br/>
                            <span id="h4-3">힐링,</span><br/>
                            <span id="h4-4">플레이스</span>
                        </h4>
                        
                    </div>
                    <div className="mapFrame">
                        <iframe className="map" src="../map.html" frameBorder="0" />
                    </div>
                </div>
            </div>
        );
    }
}

export default Main;
