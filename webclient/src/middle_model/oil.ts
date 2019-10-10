import {
    XYMidMode,
    PointMidModel
} from "./coordinate"
import fecha from 'fecha';
import { ElDropdownMenu } from 'element-ui/types/dropdown-menu';
/**
 * 溢油 mid model
 *
 * @class OilMidModel
 */
class OilMidModel {
    public time: Date
    public status: number
    public code: string
    public latlon: number[]
    public current: XYMidMode
    public wind: XYMidMode
    constructor(time: Date, status: number, code: string, latlon: number[], current: XYMidMode, wind: XYMidMode) {
        this.time = time;
        this.status = status;
        this.code = code;
        this.latlon = latlon;
        this.current = current;
        this.wind = wind;
    }


    toDivHtml(): string {
        var myself = this;
    //     let htmlStr = `
    //     <div id="oil_div" class=" card mb-4 col-md-4 box-shadow">
    //     <div class="card-header">溢油数据</div>
    //     <div class="card-body">
    //       <div class="row">
    //         <div class="col-md-4">时间</div>
    //         <div class="col-md-8">2019-02-23</div>
    //       </div>
    //       <div class="row">
    //         <div class="col-md-4">中心位置</div>
    //         <div class="col-md-8">18.2,112.0</div>
    //       </div>
    //       <div class="row row_footer">
    //         <div class="typhoon_footer">
    //           <div class="columnar my_primary">
    //             <div class="main_val">5.6</div>
    //             <div class="vice_vak">风速</div>
    //           </div>
    //           <div class="columnar my_success">
    //             <div class="main_val">115</div>
    //             <div class="vice_vak">风向</div>
    //           </div>
    //           <div class="columnar my_info">
    //             <div class="main_val">5.23</div>
    //             <div class="vice_vak">流速</div>
    //           </div>
    //           <div class="columnar my_danger">
    //             <div class="main_val">65</div>
    //             <div class="vice_vak">流向</div>
    //           </div>
    //         </div>
    //       </div>
    //     </div>
    //   </div>
    //     `
    //     return htmlStr;
        var htmlStr = `
        <div class="typhoon_data_div card mb-4 col-md-4 box-shadow">
                    <div class="card-header">台风数据</div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-4">时间</div>
                            <div class="col-md-8">${fecha.format(
            new Date(myself.time),
            'YYYY-MM-DD HH:mm'
        )}</div>
                        </div>
                        <div class="row">
                            <div class="col-md-4">中心位置</div>
                            <div class="col-md-8">${this.latlon}</div>
                        </div>
                        <div class="row row_footer">
                            <div class="typhoon_footer">
                                <div class="columnar">
                                    <div class="subitem_top">${this.wind}</div>
                                    <div class="subitem_foot">风速</div>
                                </div>
                                <div class="columnar">
                                    <div class="subitem_top">${this.current}</div>
                                    <div class="subitem_foot">流速</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        `
        return htmlStr
    }
}

export {
    OilMidModel
}