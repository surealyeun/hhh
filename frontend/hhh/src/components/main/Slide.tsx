import React from "react";
import "./Slide.scss";

import { Carousel } from "antd";

class Slide extends React.Component {
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
                    <div>
                        <img src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/93818837_131608151785158_3965098545993740587_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=106&_nc_ohc=wvnkNF-vXrYAX8A33uX&oh=8f358207c784034a74e842729e4ecf25&oe=5ECA5FDA" />
                    </div>
                    <div>
                        <img src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/94100839_2941295502580071_3479324562767351595_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=KNSjtdSu2UsAX8zkoXj&oh=1b4b850df518043e65cc2acabc4fa55f&oe=5ECC4C3B" />
                    </div>
                    <div>
                        <img src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/93818837_131608151785158_3965098545993740587_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=106&_nc_ohc=wvnkNF-vXrYAX8A33uX&oh=8f358207c784034a74e842729e4ecf25&oe=5ECA5FDA" />
                    </div>
                </Carousel>
            </div>
        );
    }
}

export default Slide;
