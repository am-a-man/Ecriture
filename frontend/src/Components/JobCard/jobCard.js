import React from 'react'
import { Divider, Row, Col } from '../../Theme/antdComponents'
import Assets from '../../Assets'
import { isMobile } from '../../Utils/utility'
import './jobCard.css'

export default function jobCard() {
    return (
        <Row justify="space-between" style={{
            padding: isMobile ? "1rem" : "3rem",
            background: "#FFFFFF",
            boxShadow: "rgb(0 0 0 / 10%) 0px 0px 10px",
            width: "100%",
            maxWidth: "560px",
            margin: "1rem 0"
        }}
        >
            <Col style={{ marginBottom: "1rem" }} span={24}>
                <img width="245px" src={Assets.CompanyLogos.microsoft} alt="" />
            </Col>
            <Divider />
            <Col style={{ marginBottom: "1rem", textAlign: "left" }} xs={24} md={12}>
                <div className="jobInfoCol">
                    <span>
                        job type
                    </span>
                    <h4>Internship</h4>
                </div>
            </Col>
            <Col style={{ marginBottom: "1rem", textAlign: "right" }} xs={24} md={12}>
                <div className="jobInfoCol">
                    <span>
                        role
                    </span>
                    <h4>software development engineer</h4>
                </div>
            </Col>
            <Col style={{ marginBottom: "1rem", textAlign: "left" }} xs={24} md={12}>
                <div className="jobInfoCol">
                    <span>
                        date
                    </span>
                    <h4>06/08/2021</h4>
                </div>
            </Col>
        </Row >
    )
}
