import React from "react";
import SlideImg from "./SlideImg";
import Header from "../common/Header";
import Footer from "../common/Footer";
import "./PlaceDetail.scss";

class PlaceDetail extends React.Component {
    render() {
        return (
            <div>
                <Header />
                <div className="place-detail">
                    <div className="slide">
                        <SlideImg />
                    </div>
                    <h1 className="place-name">식당 또는 장소이름</h1>
                    <div>
                        <p>간단한 설명 여기는 뭐를 팔거나 뭐를 체험할 수 있는 곳이다.</p>
                    </div>
                    <hr />
                    <div className="description">
                        <h3>Description</h3>
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
                            veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
                            commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
                            velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
                            occaecat cupidatat non proident, sunt in culpa qui officia deserunt
                            mollit anim id est laborum.
                        </p>
                    </div>
                    <br /> <hr />
                    <div className="location">
                        <h3>Location</h3>
                        <div className="map"></div>
                    </div>
                    <br /> <hr />
                    <div className="reviews">
                        <h3>Reviews</h3>
                        <div className="review"></div>
                        <div className="review"></div>
                        <div className="review"></div>
                    </div>
                    <br />
                    <br />
                    <br />
                    <br />
                </div>
                <Footer />
            </div>
        );
    }
}

export default PlaceDetail;
