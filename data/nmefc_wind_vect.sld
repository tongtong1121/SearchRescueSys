<StyledLayerDescriptor version="1.0.0"
		  xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml"
		  xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink"
		  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		  xsi:schemaLocation="http://www.opengis.net/sld ./StyledLayerDescriptor.xsd">
		   <NamedLayer>
		      <Name>windbarbs</Name>
		      <UserStyle>
		         <Title>windbarbs</Title>
		         <FeatureTypeStyle>
		            <Transformation>
		               <ogc:Function name="ras:RasterAsPointCollection">
		                  <ogc:Function name="parameter">
		                     <ogc:Literal>data</ogc:Literal>
		                  </ogc:Function>
		                  <!-- Activate the logic to recognize the emisphere -->
		                  <ogc:Function name="parameter">
		                    <ogc:Literal>emisphere</ogc:Literal>
		                    <ogc:Literal>True</ogc:Literal>
		                  </ogc:Function>
		                  <ogc:Function name="parameter">
		                    <ogc:Literal>interpolation</ogc:Literal>
		                    <ogc:Literal>InterpolationBilinear</ogc:Literal>
		                  </ogc:Function>
		                  <ogc:Function name="parameter">
		                    <ogc:Literal>scale</ogc:Literal>
		                    <ogc:Function name="Categorize">
		                     <ogc:Function name="env">
		                       <ogc:Literal>wms_scale_denominator</ogc:Literal>
		                     </ogc:Function>
		                       <ogc:Literal>16</ogc:Literal>
		                       <ogc:Literal>100000</ogc:Literal>
		                       <ogc:Literal>8</ogc:Literal>
		                       <ogc:Literal>500000</ogc:Literal>
		                       <ogc:Literal>2</ogc:Literal>
		                       <ogc:Literal>1000000</ogc:Literal>
		                       <ogc:Literal>0.5</ogc:Literal>
		                       <ogc:Literal>5000000</ogc:Literal>
		                       <ogc:Literal>0.2</ogc:Literal>
		                       <ogc:Literal>10000000</ogc:Literal>
		                       <ogc:Literal>0.1</ogc:Literal>
		                       <ogc:Literal>20000000</ogc:Literal>
		                       <ogc:Literal>0.05</ogc:Literal>
		                       <ogc:Literal>60000000</ogc:Literal>
		                       <ogc:Literal>0.02</ogc:Literal>
		                    </ogc:Function>
		                  </ogc:Function>
		               </ogc:Function>
		            </Transformation>
		            <Rule>
		               <PointSymbolizer>
		                  <Graphic>
		                     <Mark>
		                       <WellKnownName>windbarbs://default(
		                        <ogc:Function name="sqrt">
		                          <ogc:Add>
		                              <ogc:Mul>
		                                <ogc:PropertyName>x_wind_10m</ogc:PropertyName>
		                                <ogc:PropertyName>x_wind_10m</ogc:PropertyName>
		                              </ogc:Mul>
		                              <ogc:Mul>
		                                <ogc:PropertyName>y_wind_10m</ogc:PropertyName>
		                                <ogc:PropertyName>y_wind_10m</ogc:PropertyName>
		                              </ogc:Mul>
		                          </ogc:Add>
		                         </ogc:Function>)[m/s]?emisphere=
		                        <ogc:PropertyName>emisphere</ogc:PropertyName>
		                       </WellKnownName>
		                          <Stroke>
		                             <CssParameter name="stroke">000000</CssParameter>
		                             <CssParameter name="stroke-width">1</CssParameter>
		                          </Stroke>
		                       </Mark>
		                       <Size>
		                        <ogc:Function name="Categorize">
		                              <!-- Value to transform -->
		                             <ogc:Function name="sqrt">
		                              <ogc:Add>
		                                <ogc:Mul>
		                                 <ogc:PropertyName>x_wind_10m</ogc:PropertyName>
		                                 <ogc:PropertyName>x_wind_10m</ogc:PropertyName>
		                                </ogc:Mul>
		                                <ogc:Mul>
		                                 <ogc:PropertyName>y_wind_10m</ogc:PropertyName>
		                                 <ogc:PropertyName>y_wind_10m</ogc:PropertyName>
		                                </ogc:Mul>
		                              </ogc:Add>
		                             </ogc:Function>
		                              <ogc:Literal>8</ogc:Literal>
		                              <ogc:Literal>1.543333332</ogc:Literal>
		                              <ogc:Literal>32</ogc:Literal>
		                           </ogc:Function>
		                       </Size>
		                       <Rotation>
		                          <ogc:Function name="Categorize">
		                               <!-- Value to transform -->
		                               <ogc:Function name="sqrt">
		                                <ogc:Add>
		                                    <ogc:Mul>
		                                      <ogc:PropertyName>x_wind_10m</ogc:PropertyName>
		                                      <ogc:PropertyName>x_wind_10m</ogc:PropertyName>
		                                    </ogc:Mul>
		                                    <ogc:Mul>
		                                      <ogc:PropertyName>y_wind_10m</ogc:PropertyName>
		                                      <ogc:PropertyName>y_wind_10m</ogc:PropertyName>
		                                    </ogc:Mul>
		                                </ogc:Add>
		                              </ogc:Function>
		
		                               <!-- Output values and thresholds -->
		                               <ogc:Literal>0</ogc:Literal>
		                               <ogc:Literal>1.543333332</ogc:Literal>
		                                <ogc:Function name="toDegrees">
		                            <ogc:Function name="atan2">
		                            <ogc:PropertyName>x_wind_10m</ogc:PropertyName>
		                            <ogc:PropertyName>y_wind_10m</ogc:PropertyName>
		                         </ogc:Function>
		                          </ogc:Function>
		                        </ogc:Function>
		                     </Rotation>
		                  </Graphic>
		               </PointSymbolizer>
		               <PointSymbolizer>
		                  <Graphic>
		                     <Mark>
		                       <WellKnownName>circle</WellKnownName>
		                        <Fill>
		                           <CssParameter name="fill">
		                              <ogc:Literal>#ff0000</ogc:Literal>
		                           </CssParameter>
		                        </Fill>
		                     </Mark>
		                     <Size>3</Size>
		                  </Graphic>
		               </PointSymbolizer>
		            </Rule>
		         </FeatureTypeStyle>
		      </UserStyle>
		   </NamedLayer>
		</StyledLayerDescriptor>
