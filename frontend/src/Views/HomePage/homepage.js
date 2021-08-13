import React from 'react'
import { Row, Col, Form, Select, Option } from '../../Theme/antdComponents'
import { Container } from '../../Theme/Components'
import { JobCard } from '../../Components'
export default function Homepage() {
    const [searchForm] = Form.useForm()

    const onValuesChange = (changedValues, allValues) => {
        searchForm.submit();
    }

    const onFinish = (values) => {
        console.log(values);
    }
    return (
        <div style={{ width: "100%" }}>
            <Form
                layout="vertical"
                form={searchForm}
                onFinish={onFinish}
                // onFinishFailed={onFinishFailed}
                requiredMark={true}
                onValuesChange={onValuesChange}
                style={{
                    width: "100%",
                }}
            >
                <Container
                    height="60vh"
                    color="#FF512F"
                >
                    <Row style={{ padding: "1rem", width: "100%" }} gutter={[24, 0]}>
                        <Col xs={24} lg={8}>
                            <Form.Item
                                label="Company"
                                name="company"
                            >
                                <Select
                                    showSearch
                                    optionFilterProp="children"
                                    filterOption={true}
                                    size="large"
                                    showArrow={false}
                                    defaultValue="microsoft"
                                >
                                    <Option key="any" value="any">{"Any"}</Option>
                                    <Option key="microsoft" value="microsoft">{"Microsoft"}</Option>
                                </Select>
                            </Form.Item>
                        </Col>
                        <Col xs={24} lg={8}>
                            <Form.Item
                                label="Job Type"
                                name="job_type"
                            >
                                <Select
                                    showSearch
                                    optionFilterProp="children"
                                    filterOption={true}
                                    size="large"
                                    showArrow={false}
                                    defaultValue="internship"
                                >
                                    <Option key="any" value="any">{"Any"}</Option>
                                    <Option key="full_time" value="full_time">{"Full Time"}</Option>
                                    <Option key="internship" value="internship">{"Internship"}</Option>
                                </Select>
                            </Form.Item>
                        </Col>
                        <Col xs={24} lg={8}>
                            <Form.Item
                                label="Role"
                                name="role"
                            >
                                <Select
                                    showSearch
                                    optionFilterProp="children"
                                    filterOption={true}
                                    size="large"
                                    showArrow={false}
                                    defaultValue="sde"
                                >
                                    <Option key="any" value="any">{"Any"}</Option>
                                    <Option key="sde" value="sde">{"SDE"}</Option>
                                    <Option key="sde1" value="sde1">{"SDE 1"}</Option>
                                    <Option key="pm" value="pm">{"Product Manager"}</Option>
                                    <Option key="sdet" value="sdet">{"SDET"}</Option>
                                    <Option key="frontend_dev" value="frontend_dev">{"Frontend Developer"}</Option>
                                    <Option key="backend_dev" value="backend_dev">{"Backeend Developer"}</Option>
                                    <Option key="infosec" value="infosec">{"Information Security"}</Option>
                                </Select>
                            </Form.Item>
                        </Col>
                    </Row >
                </Container >
            </Form>
            <Container color="#fff">
                <JobCard />
                <JobCard />
                <JobCard />
                <JobCard />
            </Container>
        </div >
    )
}