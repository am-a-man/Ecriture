import React from 'react'
import { isMobile } from '../../../Utils/utility'

export default function Container({ children, color, height, ...rest }) {
    const containerStyle = {
        padding: isMobile ? "0" : "0 15%",
        maxWidth: "1600px",
        display: "flex",
        width: "100%",
        alignItems: "center",
        justifyContent: "center",
        flexDirection: "column",
        height: height,
        background: color,
    }
    return (
        <div
            style={{
                width: "100%",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
            }}
        >
            <div
                style={containerStyle}
                {...rest}
            >
                {children}
            </div>
        </div>
    )
}
