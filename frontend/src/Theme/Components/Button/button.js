import React from 'react'
import AntdButton from 'antd/lib/button'

function Button({ children, ...rest }) {
    return (
        <AntdButton {...rest}>
            {children}
        </AntdButton>
    )
}

export { Button }
