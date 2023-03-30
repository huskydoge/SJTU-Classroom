<!-- vue 3 引入百度api -->
<template>
<!--  TODO 怎么定位到铆点？？-->
  <div style="height: 500px;width:75%" id="allmap"></div>
</template>

<script>
import { defineComponent, onMounted } from "vue";
export default defineComponent({
  props:{
    points: {
      type: Array
    },
  },
  setup(props) {
    onMounted(() => {
      loadMapScript(props.points); // 加载百度地图资源
    });
    // 初始化地图
    const init = (p) => {
      let BMap = window.BMap; // 注意要带window，不然会报错（注意官方api,会有改动，之前是Bmap,后面3.0版本改为了BMap,最好查文档或者打印一下window）
      // var point = new BMap.Point(121.444695,31.027936)
      var point = new BMap.Point(p[0],p[1])
      var map = new BMap.Map("allmap"); // allmap必须和dom上的id一直
      map.centerAndZoom(
          point,
          20
      ); // 初始化地图,设置中心点坐标和地图级别

      // 标记地图点位
      const marker = new BMap.Marker(point)
      // eslint-disable-next-line no-undef
      marker.setAnimation(BMAP_ANIMATION_BOUNCE);//跳动的动画
      map.addOverlay(marker)
      // const opts = {
      //   width: 100,
      //   height: 50
      // }
      // var infoWindow = new BMap.InfoWindow('这里显示地址详细信息', opts)
      // map.openInfoWindow(infoWindow, point) // 开启信息窗口
      // marker.addEventListener('click', function() {
      //   map.openInfoWindow(infoWindow, point) // 开启信息窗口
      // })
      /////
      var scaleCtrl = new BMap.ScaleControl();  // 添加比例尺控件
      map.addControl(scaleCtrl);
      map.addControl(new BMap.NavigationControl({
        // eslint-disable-next-line no-undef
            anchor:BMAP_ANCHOR_BOTTOM_RIGHT,//显示在右上角
        // eslint-disable-next-line no-undef
            type:BMAP_NAVIGATION_CONTROL_LARGE//显示完整的平移缩放空间
        })); // 添加缩放控件
    };
    const loadMapScript = (p) => {
      // 此处在所需页面引入资源就是，不用再public/index.html中引入
      var script = document.createElement("script");
      script.type = "text/javascript";
      script.className = "loadmap"; // 给script一个类名
      script.src =
          "https://api.map.baidu.com/getscript?v=3.0&ak=pqkhLGzgZVqioQGs737I5YT5lbNfgRaU";
      // 此处需要注意：申请ak时，一定要应用类别一定要选浏览器端，不能选服务端，不然地图会报ak无效
      script.onload = () => {
        // 使用script.onload，待资源加载完成，再初始化地图
        init(p);
      };
      let loadmap = document.getElementsByClassName("loadmap");
      if (loadmap) {
        // 每次append script之前判断一下，避免重复添加script资源标签
        for (var i = 0; i < loadmap.length; i++) {
          document.body.removeChild(loadmap[i]);
        }
      }
      document.body.appendChild(script);
    };
  },
});
</script>
<style lang='less' scoped>
#allmap {
  // 注意给dom宽高，不然地图不出来
  width: 100%;
  height: 100%;
}
</style>