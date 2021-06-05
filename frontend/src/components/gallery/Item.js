const Item = ({item}) => {
    // console.log(item)
    return (
        <div className='item'>
            <a href={item.src.original}>
                <img alt='' src={item.src.medium}/>
                <h3>{item.photographer}</h3>
            </a>
        </div>
    )
}

export default Item
