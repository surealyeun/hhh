import React from "react";
import "./Slide.scss";

import { Carousel } from "antd";

interface Props{
    photos: Array<string>
}

class Slide extends React.Component<Props> {
    responsive = {
        desktop: {
            breakpoint: { max: 3000, min: 1024 },
            items: 3,
        },
        tablet: {
            breakpoint: { max: 1024, min: 464 },
            items: 2,
        },
        mobile: {
            breakpoint: { max: 464, min: 0 },
            items: 1,
        },
    };

    render() {
        return (
            <div className="Slide">
                <Carousel 
                    // draggable
                    infinite
                    arrows={true}
                    >
                    {/* <div id="img">
                        <img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F9961DA345D578B0C24" alt="1" />
                    </div> */}
                    {this.props.photos.map((img) => {
                        return (
                            <div id="img">
                                <img src={img} alt="phptos"/>
                            </div>
                        )
                    })}
                </Carousel>
            </div>
        );
    }
}

export default Slide;
