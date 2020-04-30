/*global kakao*/
import React from "react";
import { Link } from "react-router-dom";
import Header from "../common/Header";
import { Row, Col, Button, Rate } from "antd";
import "./PlaceDetail.scss";
import axios from "axios";

const URL = "http://13.125.113.171:8000/";

class PlaceDetail extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      store_name: "",
      category: "",
      address_see: "",
      address_gu: "",
      address_dong: "",
      latitude: "",
      longitude: "",
      imageList: [],
      idList: [],
      rateValue: "",
      userValue: 0,
    };
  }
  async componentDidMount() {
    await axios
      .get(
        `http://13.125.113.171:8000/dining/stores/${this.props.match.params.id}/`
      )
      .then((resp) => {
        this.setState({
          store_name: resp.data.store_name,
          category: resp.data.category,
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
        `http://13.125.113.171:8000/store/detail/${this.props.match.params.id}`
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
        `http://13.125.113.171:8000/store/score/${this.props.match.params.id}`
      )
      .then((res) => {
        if (res.data !== "undefined") {
          const num = res.data;
          this.setState({ rateValue: num.toFixed(1) });
        } else {
          this.setState({ rateValue: "0" });
        }
      });
  }

  async handleChange(e) {
    const username = sessionStorage.getItem("username");
    if (!username) {
      alert("별점은 로그인 후 남길 수 있어요!");
    } else {
      this.setState({ userValue: e });
      await axios.post(
        `${URL}wishlist/store/${this.props.match.params.id}/${username}/${e}`
      );

      await axios
        .get(
          `http://13.125.113.171:8000/store/score/${this.props.match.params.id}`
        )
        .then((res) => {
          if (res.data !== "undefined") {
            const num = res.data;
            this.setState({ rateValue: num.toFixed(1) });
          } else {
            this.setState({ rateValue: "0" });
          }
        });

      const changeText = document.querySelector(".changeText");
      changeText.innerHTML = "별점이 반영되었습니다.";
    }
  }

  render() {
    const id = this.props.match.params.id;
    const store_name = this.state.store_name;

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

    const empty = [];
    empty.push(
      <Row gutter={16}>
        <Col span={24}>
          <div className="empty" />
        </Col>
      </Row>
    );

    const empty2 = [];
    empty2.push(
      <Row gutter={16}>
        <Col span={24}>
          <div className="empty2" />
        </Col>
      </Row>
    );

    return (
      <>
        <Header />
        <div className="place-detail">
          <Row>
            <Col span={11}>
              {empty}
              <Row gutter={16}>{items}</Row>
              {empty2}
              <Row gutter={16}>{items2}</Row>
              {empty2}
              <Row gutter={16}>{items3}</Row>
            </Col>
            <Col span={1} />
            <Col span={12}>
              {empty}
              <h1 className="place-name">{this.state.store_name}</h1>
              <div>
                <span>{this.state.category}</span> &nbsp;
                <img
                  width="20px"
                  src="https://www.shwattialamal.com/wp-content/uploads/2017/08/orange-rating-star-512.png"
                />
                &nbsp;{this.state.rateValue}
                <br />
                <Rate
                  value={this.state.userValue}
                  className="rate"
                  onChange={this.handleChange.bind(this)}
                />
                &nbsp;&nbsp;
                <span class="changeText">지금 바로 별점을 남겨보세요!</span>
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
                  {sessionStorage.getItem("username") ? (
                    <Link
                      to={{
                        pathname: `/writePost`,
                        state: {
                          isStore: true,
                          id,
                          store_name,
                        },
                      }}
                    >
                      <Button>리뷰 작성하기</Button>
                    </Link>
                  ) : (
                    <Link
                      to={{
                        pathname: "/login",
                        state: {
                          isStore: true,
                          id,
                        },
                      }}
                    >
                      <Button>로그인하고 리뷰 작성하기</Button>
                    </Link>
                  )}
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
