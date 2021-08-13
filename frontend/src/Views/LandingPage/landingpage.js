import React from 'react'
import Assets from '../../Assets'
import './landingPage.css'

import { Row, Col, } from '../../Theme/antdComponents'
import { isMobile } from '../../Utils/utility'

export default function Landingpage() {

    const colStyle = {
        height: isMobile ? "45vh" : "100%",
        padding: "0 2rem",
        display: "flex",
        alignItems: "center",
        justifyContent: isMobile ? "flex-end" : "center"
    }

    return (
        <div className="landing-container">
            <Row
                style={{
                    height: "90vh"
                }}
            >
                <Col
                    xs={24}
                    md={12}
                    style={colStyle}
                >
                    <img
                        alt="logo"
                        style={{
                            width: "50%",
                            zIndex: "-1",
                            position: "absolute"
                        }}
                        src={Assets.Images.forWork} />
                </Col>
                <Col
                    xs={24}
                    md={12}
                    style={{ ...colStyle, position: "relative" }}
                >
                    <h1
                        style={!isMobile ? {
                            transform: "rotate(90deg)",
                            position: "absolute",
                            top: "20vh",
                            right: "0"
                        } : {
                            color: "#fff",
                            fontSize: "18px"
                        }}
                        className="landing-support-content">
                        {"find jobs"}
                        <br />
                        <span>{"that you need"}</span>
                    </h1>
                </Col>
            </Row>
            {
                true && <img
                    alt="background"
                    style={{
                        position: "absolute",
                        right: "0",
                        height: "800px",
                        bottom: "0",
                        zIndex: '-2',
                    }}
                    src={Assets.Images.backgroundImage}
                />
            }
        </div >

    )
}
