import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import { useState } from 'react'

const SearchBar = ({search}) => {
    const [label, setLabel] = useState('')

    const onSubmit = async(e) => {
        e.preventDefault()

        search({label})

        setLabel('')
    }

    return (
        <form onSubmit={onSubmit}>
            <input type="text" placeholder="Search" onChange={
                (e) =>setLabel(e.target.value)
            }></input>
             {/* <input className='btn btn-block' 
                type='submit' 
                value='Save Task'></input> */}
            <FontAwesomeIcon className='icon' icon={faSearch} />
        </form>
    )
}

export default SearchBar