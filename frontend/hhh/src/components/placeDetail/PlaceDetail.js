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
      location_name: "",
      description: "",
      address_see: "",
      address_gu: "",
      address_dong: "",
      latitude: "",
      longitude: "",
      imageList: [],
      idList: [],
      rateValue: 3,
    };
  }
  async componentDidMount() {
    await axios
      .get(
        `http://13.125.113.171:8000/places/location/${this.props.match.params.id}/`
      )
      .then((resp) => {
        this.setState({
          location_name: resp.data.location_name,
          description: resp.data.description,
          address_see: resp.data.address_see,
          address_gu: resp.data.address_gu,
          address_dong: resp.data.address_dong,
          latitude: resp.data.latitude,
          longitude: resp.data.longitude,
        });
      });

    const script = document.createElement("script");
    script.async = true;
    script.src = `http://dapi.kakao.com/v2/maps/sdk.js?appkey=b725b485b0888987cdae1e2ddb72374b&autoload=false`;
    document.head.appendChild(script);

    script.onload = () => {
      kakao.maps.load(() => {
        let container = document.getElementById("Mymap");
        let options = {
          center: new kakao.maps.LatLng(
            this.state.latitude,
            this.state.longitude
          ),
          level: 2,
        };

        const map = new window.kakao.maps.Map(container, options);

        // 마커가 표시될 위치입니다
        var markerPosition = new kakao.maps.LatLng(
          this.state.latitude,
          this.state.longitude
        );

        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({
          position: markerPosition,
        });

        // 마커가 지도 위에 표시되도록 설정합니다
        marker.setMap(map);
      });
    };

    // 리뷰 이미지 뽑기
    await axios
      .get(
        `http://13.125.113.171:8000/location/detail/${this.props.match.params.id}`
      )
      .then((resp) => {
        console.log(resp);
        this.setState({ rateValue: resp.score_avg });
        for (let index = 0; index < resp.data.length; index++) {
          this.setState({
            imageList: [...this.state.imageList, resp.data[index].image],
            idList: [...this.state.idList, resp.data[index].id],
          });
        }
      });

    // 별점 가져오기
    await axios
      .get(
        `http://13.125.113.171:8000/location/score/${this.props.match.params.id}`
      )
      .then((res) => this.setState({ rateValue: res.data }));
  }

  render() {
    const id = this.props.match.params.id;
    const store_name = this.state.location_name;

    const items = [];
    for (let index = 0; index < 3; index++) {
      items.push(
        <Col className="gutter-row" span={8}>
          <Link to={`/feedDetail/${this.state.idList[index]}`}>
            <img src={this.state.imageList[index]} />
          </Link>
        </Col>
      );
    }

    const items2 = [];
    for (let index = 3; index < 6; index++) {
      items2.push(
        <Col className="gutter-row" span={8}>
          <Link to={`/feedDetail/${this.state.idList[index]}`}>
            <img src={this.state.imageList[index]} />
          </Link>
        </Col>
      );
    }

    const items3 = [];
    for (let index = 6; index < 9; index++) {
      items3.push(
        <Col className="gutter-row" span={8}>
          <Link to={`/feedDetail/${this.state.idList[index]}`}>
            <img src={this.state.imageList[index]} />
          </Link>
        </Col>
      );
    }

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
              <Row gutter={16}>{items}</Row>
              <Row gutter={16}>
                <Col span={24}>
                  <div className="empty2" />
                </Col>
              </Row>
              <Row gutter={16}>{items2}</Row>
              <Row gutter={16}>
                <Col span={24}>
                  <div className="empty2" />
                </Col>
              </Row>
              <Row gutter={16}>{items3}</Row>
            </Col>
            <Col span={1} />
            <Col span={12}>
              <Row gutter={16}>
                <Col span={24}>
                  <div className="empty" />
                </Col>
              </Row>
              <h1 className="place-name">{this.state.location_name}</h1>
              <div>
                <span>{this.state.description}</span> &nbsp;
                <Rate value={this.state.rateValue} className="rate" />
              </div>
              <hr />
              <div className="location">
                <h3>Location</h3>
                <p>
                  {this.state.address_see} {this.state.address_gu}{" "}
                  {this.state.address_dong}
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
                        isStore: false,
                        id,
                        store_name,
                      },
                    }}
                  >
                    <Button>리뷰 작성하기</Button>
                  </Link>
                </div>
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
