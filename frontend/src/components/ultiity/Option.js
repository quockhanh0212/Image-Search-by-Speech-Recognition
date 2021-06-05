import Button from '../basic/Button'

const Option = ({option1, setOption1, option2, setOption2, setIsPredicted, setGallery}) => {
    function chooseOption1 () {
        setOption1(true)
        setOption2(false)
        setIsPredicted(false)
        setGallery([])
    }

    function chooseOption2() {
        setOption1(false)
        setOption2(true)
        setIsPredicted(false)
        setGallery([])
    }

    return (
        <div className="option">
            <h3>Choose Option</h3>

            <Button 
            text={'Record'}
            color={ option1 ? 'green' : 'red'}
            onClick={chooseOption1}/>
    
            <Button 
            text={'Upload your file'}
            color={ option2 ? 'green' : 'red'}
            onClick={chooseOption2}/>
        </div>
    )
}

export default Option
