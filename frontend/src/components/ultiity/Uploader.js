import {  useState } from 'react'

const Uploader = ({onFileUpload}) => {

    const [selectedFiles, setSelectedFiles] = useState(null)


    const onChange = (e) => {
        e.preventDefault()

        setSelectedFiles(e.target.files)
    }

    const onClick = (e) => {
        e.preventDefault()

        onFileUpload(selectedFiles)
    }

    return (
        <div className='uploader'>
            <h3>Option 2: Upload your file</h3>
            <input type="file" onChange={onChange} />
            <button  onClick={onClick}>Upload</button>
        </div>
    )
}

export default Uploader
