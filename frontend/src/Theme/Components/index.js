import React from 'react'
import { Button } from './Button/button'
import Drawer from 'antd/lib/drawer'
import { Link as RouteLink } from 'react-router-dom'
import Container from './Container/container'

const Link = ({ children, ...rest }) => {
    return <RouteLink
        style={{
            fontWeight: 600,
            textTransform: "uppercase",
        }}
        {...rest}>
        {children}
    </RouteLink>
}


export { Button, Drawer, Link, Container }