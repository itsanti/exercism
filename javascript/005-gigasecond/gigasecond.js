//
// This is only a SKELETON file for the 'Gigasecond' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const gigasecond = (startDate) => {
  //return new Date(startDate.getTime() + 1e12);  
  return new Date(+startDate + Math.pow(10, 12));
};
