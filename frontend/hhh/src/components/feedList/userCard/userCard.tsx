import React from 'react';
import './userCard.scss';

class UserCard extends React.Component {
    render() {
        return (
            <div id="user-card">
                <div id="avatar"></div>
                <div id="user-info">
                    <div id="user-id"></div>
                </div>
            </div>
        );
    }
}

export default UserCard;