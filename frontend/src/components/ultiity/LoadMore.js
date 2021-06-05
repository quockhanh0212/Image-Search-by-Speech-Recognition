import Button from '../basic/Button'

const LoadMore = ({loadMore}) => {
    const onClick = async(e) => {
        e.preventDefault()
        loadMore()
    }

    return (
       <div>
           <button className="load-more" onClick={onClick}>Load more</button>
       </div>
    )
}

export default LoadMore
