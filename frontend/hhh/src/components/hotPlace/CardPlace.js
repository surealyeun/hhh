import React from "react";
import { Link } from "react-router-dom";
import "./Card.scss";

const Place = ({ state }) => {
  const {
    id,
    location_name,
    description,
    address_see,
    address_gu,
    address_dong,
    url,
    latitude,
    longitude,
  } = state;

  return (
    <div className="box">
      <div>
        <div class="image">
          <Link
            to={{
              pathname: `/place/${id}`,
              state: {
                location_name,
                description,
                address_see,
                address_gu,
                address_dong,
                latitude,
                longitude,
              },
            }}
          >
            <img src="https://lh3.googleusercontent.com/proxy/45fNF_FYlyMXvdJCluKICrb-zWoyDzujodnKlRjrxOUl3NJ5BQ3ZPLlzK6TeyYdiT-FHwG4QFQrW3f139BFn-vUP36aja_455PaaCrRXKF7Vsj7E7FbBlgEwp3b0THNYH48VunIllChQCpPWNW1FOg" />
            <h2>
                <span className="small">{description}</span>
                <br />
              <span>
                {location_name}
              </span>
            </h2>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Place;
