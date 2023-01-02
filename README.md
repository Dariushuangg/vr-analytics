# VR User Analytics
I worked as a research assistant at [Professor Gorlatova's I^3T Lab](https://maria.gorlatova.com/facilities-and-resources/) on a VR simulation research project. As we evaluate test subject's cognitive states during experiments, one recurrent question I encountered is "how can we better understand user's behaviors when performing tasks in VR"? I created this github project out of the code I wrote for the lab to develop a perhaps more generally applicable workflow of analyzing VR user behavior.
## Project Architecture
By installing the C# data collector script to your Unity project, you will be able to gather raw data on **where the user is looking at**, **where the user is touching**, **how long did a user take to accomplish a certain task** etc. during your VR experience. Then, you may run the Python analyzer scripts to obtain insights from on these raw data; For instance, I analyzed how frequently does a "focus switch" occurs for the user. 
![image](https://user-images.githubusercontent.com/111829337/203881824-4266cbfc-05a8-441a-8036-f1a2d29f4f35.png)
## Use Cases
Existing use cases: This project was used in an extension study of the case study in [ISMAR 2022 paper](https://maria.gorlatova.com/wp-content/uploads/2022/08/ISMAR2022aGorlatova_IntegratedDesign.pdf) authored by [Tim Scargill](https://sites.duke.edu/timscargill/).
In that study, researchers were interested in how the test subjects' abilities to focus on educational content are influenced by the simulated environment. 
</br>
</br>
<img align="left" width="450" height="400" src="https://user-images.githubusercontent.com/111829337/203883019-5e42a356-c8fe-4e5c-b82a-da466939dd12.png">
<img align="left" width="450" height="400" src="https://user-images.githubusercontent.com/111829337/203883031-efec7e1c-b094-408a-a764-0e285da01bb8.png">
</br>
</br>
