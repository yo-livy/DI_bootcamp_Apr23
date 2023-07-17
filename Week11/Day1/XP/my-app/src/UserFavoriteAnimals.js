const UserFavouriteAnimals = (props) => {
    const { animals } = props
    return (
      // Mapping through the animals array and returning JSX for each item
      <ul>
        {animals.map((item, index) => {
        return (
          // Adding a unique key prop to the parent div element
         
            <li key={index}>{item}</li>
          
        );
        })}
        </ul>
    );
  };
  
  export default UserFavouriteAnimals;
  