import React from "react";

import { Carousel } from 'react-responsive-carousel';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import "./SlideImg.scss";

class SlideImg extends React.Component {
    render() {
        return (
            <div className="slide-img">
                <Carousel
                    showThumbs={false}
                    infiniteLoop={true}
                    centerMode={true}
                    showStatus={false}
                >
                <div>
                    <img src="https://lh3.googleusercontent.com/proxy/9BsLs6fNt3UXrEeUqh7TP7o5LO6tnOEp_g2uor6DxppXjNbebyQYSrKCzIS8f4Lijg0W8-lv8fjaVUrJXX0iOFIxBXnbDRShG3A-nZEY9ZBIZ0EQPFU-gf5MMouaL4pjqmZW3eStCeJ2sbGpeKp0kII92F2R4AXtu0TwfcX9VV-6ALBS7sgQaIqLPbn2i9SkptuoLBbHkVprO_ABDLx3EYSN55QUU6IBBNi7jg7L9n8Dk-_k2Y3o_hp5A76r57k-rkKiZU4mbxzPF1bwTuXb_hxMcSGvw9Tx9-JwjrRJKpCemg0NCygsdGoQ" />
                    
                </div>
                <div>
                    <img src="https://www.thebling.co.kr/wp-content/uploads/2018/03/BSV5376-1500x1000.jpg" />
                    
                </div>
                </Carousel>
            </div>
        );
    }
}

export default SlideImg;
