/*global kakao*/
import React from "react";
import { Row, Col } from "antd";
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
        var markerPosition = new kakao.maps.LatLng(
          this.props.location.state.latitude,
          this.props.location.state.longitude
        );

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
    const state = this.props.location.state;
    console.log(this.props);
    return (
      <div className="place-detail">
        <Row>
          <Col span={11}>
            <Row gutter={16}>
              <Col span={24}>
                <div className="empty" />
              </Col>
            </Row>
            <Row gutter={16}>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-atl3-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/92028574_152110496140923_1238325184368526124_n.jpg?_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=103&_nc_ohc=LUKxaXWCmbcAX8-aYm4&oh=977f61027864985c24962340097d8d67&oe=5EAF8F10" />
              </Col>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-atl3-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/91523822_505695946973748_4618136914309432735_n.jpg?_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=100&_nc_ohc=cPwyIMYbdNYAX9KR5r2&oh=fb055704713c3bac2169e00bc0240288&oe=5EB23135" />
              </Col>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/e35/92462223_1528148800680967_6557145994758711521_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=107&_nc_ohc=JdQcb32YsjQAX-cVqAp&se=7&oh=6e0fed0ff2eee3ce4082ea3443aea6ca&oe=5EC8448A&ig_cache_key=MjI4MjA5MzUwOTY0NTE1MjI4OQ%3D%3D.2" />
              </Col>
            </Row>
            <Row gutter={16}>
              <Col span={24}>
                <div className="empty2" />
              </Col>
            </Row>
            <Row gutter={16}>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/e35/92210321_222417495485454_8828049053151549869_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=106&_nc_ohc=CnP67USwd1IAX81Nxu2&se=7&oh=3898693d80c33942fa0f210514761fa2&oe=5EC8B1B2&ig_cache_key=MjI4MjA4ODcxNDU1NjE2NjgxNQ%3D%3D.2" />
              </Col>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/e35/91978608_134913158084830_2765144029097195256_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=110&_nc_ohc=ty1JqScPtV4AX93Ofmi&se=7&oh=0001d19bae32e84886ae40e8cbac128e&oe=5EC68058&ig_cache_key=MjI4MjA3OTU0MDY2NTAyODkxOQ%3D%3D.2" />
              </Col>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/e35/92566770_152891716088094_2844173153369313983_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=106&_nc_ohc=ZZkRYv-1cbIAX-m9SUQ&se=7&oh=53999d87196f8279985b3466189798e1&oe=5EC64B2E&ig_cache_key=MjI4MjA3NDk4Mzc0NzYwMzIxOA%3D%3D.2" />
              </Col>
            </Row>
            <Row gutter={16}>
              <Col span={24}>
                <div className="empty2" />
              </Col>
            </Row>
            <Row gutter={16}>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-yyz1-1.cdninstagram.com/v/t51.2885-15/e35/92245979_831655963994693_5110124155454270836_n.jpg?_nc_ht=scontent-yyz1-1.cdninstagram.com&_nc_cat=105&_nc_ohc=DdXoCoMV2PQAX9yZK1p&se=7&oh=90a8bd1df431c150c3a022c304bf9f96&oe=5EC655DE&ig_cache_key=MjI4MjAwNjAwNDIwNjEyNTUzMQ%3D%3D.2" />
              </Col>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-yyz1-1.cdninstagram.com/v/t51.2885-15/e35/92259511_123040675996035_1076069689526094587_n.jpg?_nc_ht=scontent-yyz1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=V_ANpOZv2UcAX_7ExX5&se=8&oh=058670cfeebdec5a0873d64bd509c55d&oe=5EC5BF2D&ig_cache_key=MjI4MTgyNTU0NzcwMDMwMDc3OA%3D%3D.2" />
              </Col>
              <Col className="gutter-row" span={8}>
                <img src="https://scontent-yyz1-1.cdninstagram.com/v/t51.2885-15/e35/91909496_533547517347244_5752511906769169757_n.jpg?_nc_ht=scontent-yyz1-1.cdninstagram.com&_nc_cat=104&_nc_ohc=5i9ZJYgXnB4AX-90hWa&oh=0adf839cb81b23040ed4e09b8f832e0c&oe=5EC83B40&ig_cache_key=MjI4MTgzNjkzMTMzMzcyNjIzNg%3D%3D.2" />
              </Col>
            </Row>
          </Col>
          <Col span={1} />
          <Col span={12}>
          <Row gutter={16}>
              <Col span={24}>
                <div className="empty" />
              </Col>
            </Row>
            <h1 className="place-name">{state.store_name}</h1>
            <div>
              <p>{state.category}</p>
            </div>
            <hr />
            <div className="location">
              <h3>Location</h3>
              <p>
                {state.address_see} {state.address_gu} {state.address_dong}
              </p>
              <div className="map" id="Mymap"></div>
            </div>
            <br />
            <hr />
            <div className="reviews">
              <h3>Reviews</h3>
              <div className="review"></div>
              <div className="review"></div>
              <div className="review"></div>
            </div>
            <br /> <hr />
            <br />
            <br />
            <br />
          </Col>
        </Row>
      </div>
    );
  }
}

export default PlaceDetail;
