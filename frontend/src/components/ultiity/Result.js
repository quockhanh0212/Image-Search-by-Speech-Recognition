import React from 'react'

const Result = ({class_name}) => {
    return (
        <div className="result">
            <h3> Result </h3>
            <table>
                <tbody>
                    <tr>
                        <th>Class name</th>
                    </tr>
                    <tr>
                        <td>{class_name}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    )
}

export default Result
