<?xml version="1.0" encoding="UTF-8"?>

<xsl:transform version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <body>
                <table>
                    <tr>
                        <th>Price</th>
                        <th>Image</th>
                        <th>Description</th>
                    </tr>
                    <xsl:for-each select="data/item">
                        <tr>
                            <td>
                                <xsl:value-of select="price"/>
                            </td>
                            <td>
                                <xsl:value-of select="image"/>
                            </td>
                            <td>
                                <xsl:value-of select="description"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:transform>