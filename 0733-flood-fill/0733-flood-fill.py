class Solution(object):
    def fill_image(self, image, sr,sc, color, current):
        if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) : return
        if current!=image[sr][sc] : return
        image[sr][sc]=color
        self.fill_image(image, sr-1, sc, color, current)
        self.fill_image(image, sr+1, sc, color, current)
        self.fill_image(image, sr, sc-1, color, current)
        self.fill_image(image, sr, sc+1, color, current)


    def floodFill(self, image, sr, sc, color):
        if image[sr][sc]==color : return image
        self.fill_image(image, sr, sc, color, image[sr][sc])
        return image
        
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        