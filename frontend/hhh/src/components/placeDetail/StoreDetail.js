/*global kakao*/
import React from "react";
import "./PlaceDetail.scss";

class PlaceDetail extends React.Component {
  componentDidMount() {
    const script = document.createElement("script");
    script.async = true;
    script.src = `http://dapi.kakao.com/v2/maps/sdk.js?appkey=b725b485b0888987cdae1e2ddb72374b&autoload=false`;
    document.head.appendChild(script);

    script.onload = () => {
      kakao.maps.load(() => {
        let container = document.getElementById("Mymap");
        let options = {
          center: new kakao.maps.LatLng(
            this.props.location.state.latitude,
            this.props.location.state.longitude
          ),
          level: 2,
        };

        const map = new window.kakao.maps.Map(container, options);

        // 마커가 표시될 위치입니다
        var markerPosition = new kakao.maps.LatLng(this.props.location.state.latitude, this.props.location.state.longitude);

        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({
          position: markerPosition,
        });

        // 마커가 지도 위에 표시되도록 설정합니다
        marker.setMap(map);
      });
    };
  }

  render() {
    const id = this.props.match.params.id;
    const store_name = this.props.location.state.store_name;
    const category = this.props.location.state.category;
    console.log(this.props);
    return (
      <div className="place-detail">
        <h1 className="place-name">{store_name}</h1>
        <div>
          <p>{category}</p>
        </div>
        <hr />
        <div className="description">
          <h3>Description</h3>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </p>
        </div>
        <br /> <hr />
        <div className="location">
          <h3>Location</h3>
          <div className="map" id="Mymap"></div>
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
    );
  }
}

export default PlaceDetail;
