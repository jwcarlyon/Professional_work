import React, { Component } from 'react';
import ListCourses from './ListCourses';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Course from './Course';

class InstructionApplicationPage extends Component {
    render() {
        return (
            <div>
            <h1>Instructor Application</h1>
                <Router>
                    <Routes>
                        <Route path="/" element = {<ListCourses/>} />
                        <Route path="/courses/:id" element = {<Course/>} />
                        <Route path="/courses" element = {<ListCourses/>} />
                    </Routes>
                </Router>
            </div>
        )
    }
}

export default InstructionApplicationPage
