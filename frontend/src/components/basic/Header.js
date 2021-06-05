import PropTypes from 'prop-types'
import Button from './Button'
import {useLocation} from 'react-router-dom'
import SearchBar from '../ultiity/SearchBar'

const Header = ({title, onAdd, showAdd, search}) => {
    const location = useLocation()

    return (
        <header>
            <h1 >{title}</h1>
            {/* {location.pathname === '/' && <Button 
                color={showAdd ? 'red' : 'green'} 
                text={showAdd ? 'Close' : 'Add'}
                onClick = {onAdd}
            ></Button>} */}

        </header>
    )
}

Header.defaultProps = {
    title: 'Voice Recognition Tool', 
}

Header.prototype = {
    title: PropTypes.string.isRequired,
}

export default Header
