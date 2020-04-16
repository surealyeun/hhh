import React from "react";
import { Link } from "react-router-dom";
import "./Main.scss";

const username:string | null = sessionStorage.getItem("username");

class Main extends React.Component {
    render() {
        return (
            <div className="main">
                <div className="test">
                    <h1>TEST</h1>
                        <h4>클릭하면 해당 페이지로 넘어갑니다.</h4><br/>
                        <Link to="/login">
                        😃 유저 로그인 페이지
                        </Link><br/>
                        <Link to="/userInfo">
                        { username ? '🤟 회원 정보 페이지' : ''}
                        </Link><br/>
                        <Link to="/spotList">
                        🏛 장소 리스트 페이지
                        </Link><br/>
                        <Link to="/place">
                        🔎 장소 상세 페이지
                        </Link><br/>
                        <Link to="/feedList">
                        🙌 SNS 피드 페이지
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
