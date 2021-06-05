import Item from './Item'

const Gallery = ({items}) => {
    return (
        <div>
            <h3> Result pictures </h3>
            <div className="gallery">
            {items.map((item, index) => (
              <Item key={index} item={item} /> ))
            }    
            </div> 
        </div>
    )
}

export default Gallery
