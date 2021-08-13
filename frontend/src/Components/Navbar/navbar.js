import React, { useState } from 'react'
import './navbar.css'
import { Button, Drawer, Link } from '../../Theme/Components'
import Icons from '../../Theme/Icons/iconMap'
export default function Navbar() {
    const [visible, setVisible] = useState(false)
    const onClose = () => {
        setVisible(false)
    }
    return (
        <div className="navbar">
            <nav>
                <ul>
                    <li>
                        <Link style={{ color: "#fff", fontWeight: "600" }} to="/">4Work.</Link>
                    </li>
                    <li>
                        <Button onClick={() => setVisible(true)} shape="circle" type="link" icon={Icons.pauseOutlined({ rotate: 90 })} ></Button>
                    </li>
                </ul>
            </nav>
            <Drawer
                placement="right"
                closable={false}
                onClose={onClose}
                visible={visible}
            >
                <nav
                    style={{
                        height: "100%",
                        width: "100%",
                    }}
                >
                    <ul
                        style={{
                            height: "100%",
                            width: "100%",
                            display: "flex",
                            flexDirection: "column",
                            justifyContent: "space-evenly",
                            alignItems: "center",
                            listStyleType: "none"
                        }}
                    >
                        <li>
                            <Link onClick={onClose} to="/">Landing</Link>
                        </li>
                        <li>
                            <Link onClick={onClose} to="/home">Home Page</Link>
                        </li>
                    </ul>
                </nav>
            </Drawer>
        </div >
    )
}
