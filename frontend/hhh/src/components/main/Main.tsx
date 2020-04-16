import React from "react";
import { Link } from "react-router-dom";
import "./Main.scss";

class Main extends React.Component {
    render() {
        return (
            <div className="main">
                <div className="test">
                    <h1>TEST</h1>
                        <h4>클릭하면 해당 페이지로 넘어갑니다.</h4>
                        <Link to="/login">
                            1. 유저 로그인 페이지
                        </Link><br/>
                        <Link to="/userInfo">
                            2. 회원 정보 수정 페이지
                        </Link><br/>
                        <Link to="/spotList">
                            3. 장소 리스트 페이지
                        </Link><br/>
                        <Link to="/place">
                            4. 장소 상세 페이지
                        </Link><br/>
                        <Link to="/feedList">
                            5. SNS 피드 페이지
                        </Link>
                </div>
                <div className="grid">
                    <div className="title">
                        <h1>
                            ㅎ<br />ㅎ<br />ㅎ
                        </h1>
                        <h4>
                            <span id="h4-1">핫,</span>
                            <br />
                            <span id="h4-2">힙,</span>
                            <br />
                            <span id="h4-3">힐링,</span>
                            <br />
                            <span id="h4-4">플레이스</span>
                        </h4>
                        <hr />
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
