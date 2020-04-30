/*global kakao*/
import React from "react";
import { Link } from "react-router-dom";
import Header from "../common/Header";
import { Row, Col, Button, Rate } from "antd";
import "./PlaceDetail.scss";
import axios from "axios";

class PlaceDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      imageList: [],
    };
  }
  async componentDidMount() {
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

    await axios
      .get(
        `http://13.125.113.171:8000/store/detail/${this.props.match.params.id}`
      )
      .then((resp) => {
        for (let index = 0; index < resp.data.length; index++) {
          this.setState({
            imageList: [...this.state.imageList, resp.data[index].image],
          });
        }
      });
  }

  render() {
    const id = this.props.match.params.id;
    const state = this.props.location.state;
    const store_name = state.store_name;
    const area = state.area;
    return (
      <>
        <Header />
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
                  <img src={this.state.imageList[0]} />
                </Col>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[1]} />
                </Col>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[2]} />
                </Col>
              </Row>
              <Row gutter={16}>
                <Col span={24}>
                  <div className="empty2" />
                </Col>
              </Row>
              <Row gutter={16}>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[3]} />
                </Col>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[4]} />
                </Col>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[5]} />
                </Col>
              </Row>
              <Row gutter={16}>
                <Col span={24}>
                  <div className="empty2" />
                </Col>
              </Row>
              <Row gutter={16}>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[6]} />
                </Col>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[7]} />
                </Col>
                <Col className="gutter-row" span={8}>
                  <img src={this.state.imageList[8]} />
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
                <span>{state.category}</span> &nbsp;
                <Rate value="4" className="rate" />
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
                <div className="review">
                  <Link
                    to={{
                      pathname: `/writePost`,
                      state: {
                        isStore: true,
                        area,
                        store_name,
                        id,
                        state,
                      },
                    }}
                  >
                    <Button>리뷰 작성하기</Button>
                  </Link>
                </div>
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
      </>
    );
  }
}

export default PlaceDetail;
