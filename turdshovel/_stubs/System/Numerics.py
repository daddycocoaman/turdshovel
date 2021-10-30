# encoding: utf-8
# module System.Numerics calls itself Numerics
# from System.Numerics.Vectors, Version=4.1.4.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
# no doc
# no imports

# functions

def Vector(*args, **kwargs): # real signature unknown
    """ Provides a collection of static convenience methods for creating, manipulating, combining, and converting generic vectors. """
    pass

# classes

class Matrix3x2(object, IEquatable[Matrix3x2]):
    """
    Represents a 3x2 matrix.
    
    Matrix3x2(m11: Single, m12: Single, m21: Single, m22: Single, m31: Single, m32: Single)
    """
    @staticmethod
    def Add(value1, value2):
        """
        Add(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2
        
            Adds each element in one matrix with its corresponding element in a second matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix that contains the summed values of value1value1 and value2value2.
        """
        pass

    @staticmethod
    def CreateRotation(radians, centerPoint=None):
        """
        CreateRotation(radians: Single) -> Matrix3x2
        
            Creates a rotation matrix using the given rotation in radians.
        
            radians: The amount of rotation, in radians.
            Returns: The rotation matrix.
        CreateRotation(radians: Single, centerPoint: Vector2) -> Matrix3x2
        
            Creates a rotation matrix using the specified rotation in radians and a center point.
        
            radians: The amount of rotation, in radians.
            centerPoint: The center point.
            Returns: The rotation matrix.
        """
        pass

    @staticmethod
    def CreateScale(*__args):
        """
        CreateScale(xScale: Single, yScale: Single) -> Matrix3x2
        
            Creates a scaling matrix from the specified X and Y components.
        
            xScale: The value to scale by on the X axis.
            yScale: The value to scale by on the Y axis.
            Returns: The scaling matrix.
        CreateScale(xScale: Single, yScale: Single, centerPoint: Vector2) -> Matrix3x2
        
            Creates a scaling matrix that is offset by a given center point.
        
            xScale: The value to scale by on the X axis.
            yScale: The value to scale by on the Y axis.
            centerPoint: The center point.
            Returns: The scaling matrix.
        CreateScale(scales: Vector2) -> Matrix3x2
        
            Creates a scaling matrix from the specified vector scale.
        
            scales: The scale to use.
            Returns: The scaling matrix.
        CreateScale(scales: Vector2, centerPoint: Vector2) -> Matrix3x2
        
            Creates a scaling matrix from the specified vector scale with an offset from the specified center point.
        
            scales: The scale to use.
            centerPoint: The center offset.
            Returns: The scaling matrix.
        CreateScale(scale: Single) -> Matrix3x2
        
            Creates a scaling matrix that scales uniformly with the given scale.
        
            scale: The uniform scale to use.
            Returns: The scaling matrix.
        CreateScale(scale: Single, centerPoint: Vector2) -> Matrix3x2
        
            Creates a scaling matrix that scales uniformly with the specified scale with an offset from the specified center.
        
            scale: The uniform scale to use.
            centerPoint: The center offset.
            Returns: The scaling matrix.
        """
        pass

    @staticmethod
    def CreateSkew(radiansX, radiansY, centerPoint=None):
        """
        CreateSkew(radiansX: Single, radiansY: Single) -> Matrix3x2
        
            Creates a skew matrix from the specified angles in radians.
        
            radiansX: The X angle, in radians.
            radiansY: The Y angle, in radians.
            Returns: The skew matrix.
        CreateSkew(radiansX: Single, radiansY: Single, centerPoint: Vector2) -> Matrix3x2
        
            Creates a skew matrix from the specified angles in radians and a center point.
        
            radiansX: The X angle, in radians.
            radiansY: The Y angle, in radians.
            centerPoint: The center point.
            Returns: The skew matrix.
        """
        pass

    @staticmethod
    def CreateTranslation(*__args):
        """
        CreateTranslation(position: Vector2) -> Matrix3x2
        
            Creates a translation matrix from the specified 2-dimensional vector.
        
            position: The translation position.
            Returns: The translation matrix.
        CreateTranslation(xPosition: Single, yPosition: Single) -> Matrix3x2
        
            Creates a translation matrix from the specified X and Y components.
        
            xPosition: The X position.
            yPosition: The Y position.
            Returns: The translation matrix.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Matrix3x2, other: Matrix3x2) -> bool
        
            Returns a value that indicates whether this instance and another 3x2 matrix are equal.
        
            other: The other matrix.
            Returns: true if the two matrices are equal; otherwise, false.
        Equals(self: Matrix3x2, obj: object) -> bool
        
            Returns a value that indicates whether this instance and a specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: true if the current instance and objobj are equal; otherwise, false. If objobj is null, the method returns false.
        """
        pass

    def GetDeterminant(self):
        """
        GetDeterminant(self: Matrix3x2) -> Single
        
            Calculates the determinant for this matrix.
            Returns: The determinant.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Matrix3x2) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code.
        """
        pass

    @staticmethod
    def Invert(matrix, result):
        """
        Invert(matrix: Matrix3x2) -> (bool, Matrix3x2)
        
            Inverts the specified matrix. The return value indicates whether the operation succeeded.
        
            matrix: The matrix to invert.
            Returns: true if matrixmatrix was converted successfully; otherwise,  false.
        """
        pass

    @staticmethod
    def Lerp(matrix1, matrix2, amount):
        """
        Lerp(matrix1: Matrix3x2, matrix2: Matrix3x2, amount: Single) -> Matrix3x2
        
            Performs a linear interpolation from one matrix to a second matrix based on a value that specifies the weighting of the second matrix.
        
            matrix1: The first matrix.
            matrix2: The second matrix.
            amount: The relative weighting of matrix2.
            Returns: The interpolated matrix.
        """
        pass

    @staticmethod
    def Multiply(value1, value2):
        """
        Multiply(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2
        
            Returns the matrix that results from multiplying two matrices together.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The product matrix.
        Multiply(value1: Matrix3x2, value2: Single) -> Matrix3x2
        
            Returns the matrix that results from scaling all the elements of a specified matrix by a scalar factor.
        
            value1: The matrix to scale.
            value2: The scaling value to use.
            Returns: The scaled matrix.
        """
        pass

    @staticmethod
    def Negate(value):
        """
        Negate(value: Matrix3x2) -> Matrix3x2
        
            Negates the specified matrix by multiplying all its values by -1.
        
            value: The matrix to negate.
            Returns: The negated matrix.
        """
        pass

    @staticmethod
    def Subtract(value1, value2):
        """
        Subtract(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2
        
            Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix containing the values that result from subtracting each element in value2value2 from its corresponding element in value1value1.
        """
        pass

    def ToString(self):
        """
        ToString(self: Matrix3x2) -> str
        
            Returns a string that represents this matrix.
            Returns: The string representation of this matrix.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, m11, m12, m21, m22, m31, m32):
        """
        __new__(cls: type, m11: Single, m12: Single, m21: Single, m22: Single, m31: Single, m32: Single)
        __new__[Matrix3x2]() -> Matrix3x2
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2
        
            Adds each element in one matrix with its corresponding element in a second matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix that contains the summed values.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2
        
            Returns the matrix that results from multiplying two matrices together.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The product matrix.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(value1: Matrix3x2, value2: Matrix3x2) -> Matrix3x2
        
            Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix containing the values that result from subtracting each element in value2value2 from its corresponding element in value1value1.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the current matrix is the identity matrix.

Get: IsIdentity(self: Matrix3x2) -> bool

"""

    Translation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the translation component of this matrix.

Get: Translation(self: Matrix3x2) -> Vector2

Set: Translation(self: Matrix3x2) = value
"""


    Identity = None
    M11 = None
    M12 = None
    M21 = None
    M22 = None
    M31 = None
    M32 = None


class Matrix4x4(object, IEquatable[Matrix4x4]):
    """
    Represents a 4x4 matrix.
    
    Matrix4x4(m11: Single, m12: Single, m13: Single, m14: Single, m21: Single, m22: Single, m23: Single, m24: Single, m31: Single, m32: Single, m33: Single, m34: Single, m41: Single, m42: Single, m43: Single, m44: Single)
    Matrix4x4(value: Matrix3x2)
    """
    @staticmethod
    def Add(value1, value2):
        """
        Add(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4
        
            Adds each element in one matrix with its corresponding element in a second matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix that contains the summed values of value1value1 and value2value2.
        """
        pass

    @staticmethod
    def CreateBillboard(objectPosition, cameraPosition, cameraUpVector, cameraForwardVector):
        """
        CreateBillboard(objectPosition: Vector3, cameraPosition: Vector3, cameraUpVector: Vector3, cameraForwardVector: Vector3) -> Matrix4x4
        
            Creates a spherical billboard that rotates around a specified object position.
        
            objectPosition: The position of the object that the billboard will rotate around.
            cameraPosition: The position of the camera.
            cameraUpVector: The up vector of the camera.
            cameraForwardVector: The forward vector of the camera.
            Returns: The created billboard.
        """
        pass

    @staticmethod
    def CreateConstrainedBillboard(objectPosition, cameraPosition, rotateAxis, cameraForwardVector, objectForwardVector):
        """
        CreateConstrainedBillboard(objectPosition: Vector3, cameraPosition: Vector3, rotateAxis: Vector3, cameraForwardVector: Vector3, objectForwardVector: Vector3) -> Matrix4x4
        
            Creates a cylindrical billboard that rotates around a specified axis.
        
            objectPosition: The position of the object that the billboard will rotate around.
            cameraPosition: The position of the camera.
            rotateAxis: The axis to rotate the billboard around.
            cameraForwardVector: The forward vector of the camera.
            objectForwardVector: The forward vector of the object.
            Returns: The billboard matrix.
        """
        pass

    @staticmethod
    def CreateFromAxisAngle(axis, angle):
        """
        CreateFromAxisAngle(axis: Vector3, angle: Single) -> Matrix4x4
        
            Creates a matrix that rotates around an arbitrary vector.
        
            axis: The axis to rotate around.
            angle: The angle to rotate around axis, in radians.
            Returns: The rotation matrix.
        """
        pass

    @staticmethod
    def CreateFromQuaternion(quaternion):
        """
        CreateFromQuaternion(quaternion: Quaternion) -> Matrix4x4
        
            Creates a rotation matrix from the specified Quaternion rotation value.
        
            quaternion: The source Quaternion.
            Returns: The rotation matrix.
        """
        pass

    @staticmethod
    def CreateFromYawPitchRoll(yaw, pitch, roll):
        """
        CreateFromYawPitchRoll(yaw: Single, pitch: Single, roll: Single) -> Matrix4x4
        
            Creates a rotation matrix from the specified yaw, pitch, and roll.
        
            yaw: The angle of rotation, in radians, around the Y axis.
            pitch: The angle of rotation, in radians, around the X axis.
            roll: The angle of rotation, in radians, around the Z axis.
            Returns: The rotation matrix.
        """
        pass

    @staticmethod
    def CreateLookAt(cameraPosition, cameraTarget, cameraUpVector):
        """
        CreateLookAt(cameraPosition: Vector3, cameraTarget: Vector3, cameraUpVector: Vector3) -> Matrix4x4
        
            Creates a view matrix.
        
            cameraPosition: The position of the camera.
            cameraTarget: The target towards which the camera is pointing.
            cameraUpVector: The direction that is &quot;up&quot; from the camera&#39;s point of view.
            Returns: The view matrix.
        """
        pass

    @staticmethod
    def CreateOrthographic(width, height, zNearPlane, zFarPlane):
        """
        CreateOrthographic(width: Single, height: Single, zNearPlane: Single, zFarPlane: Single) -> Matrix4x4
        
            Creates an orthographic perspective matrix from the given view volume dimensions.
        
            width: The width of the view volume.
            height: The height of the view volume.
            zNearPlane: The minimum Z-value of the view volume.
            zFarPlane: The maximum Z-value of the view volume.
            Returns: The orthographic projection matrix.
        """
        pass

    @staticmethod
    def CreateOrthographicOffCenter(left, right, bottom, top, zNearPlane, zFarPlane):
        """
        CreateOrthographicOffCenter(left: Single, right: Single, bottom: Single, top: Single, zNearPlane: Single, zFarPlane: Single) -> Matrix4x4
        
            Creates a customized orthographic projection matrix.
        
            left: The minimum X-value of the view volume.
            right: The maximum X-value of the view volume.
            bottom: The minimum Y-value of the view volume.
            top: The maximum Y-value of the view volume.
            zNearPlane: The minimum Z-value of the view volume.
            zFarPlane: The maximum Z-value of the view volume.
            Returns: The orthographic projection matrix.
        """
        pass

    @staticmethod
    def CreatePerspective(width, height, nearPlaneDistance, farPlaneDistance):
        """
        CreatePerspective(width: Single, height: Single, nearPlaneDistance: Single, farPlaneDistance: Single) -> Matrix4x4
        
            Creates a perspective projection matrix from the given view volume dimensions.
        
            width: The width of the view volume at the near view plane.
            height: The height of the view volume at the near view plane.
            nearPlaneDistance: The distance to the near view plane.
            farPlaneDistance: The distance to the far view plane.
            Returns: The perspective projection matrix.
        """
        pass

    @staticmethod
    def CreatePerspectiveFieldOfView(fieldOfView, aspectRatio, nearPlaneDistance, farPlaneDistance):
        """
        CreatePerspectiveFieldOfView(fieldOfView: Single, aspectRatio: Single, nearPlaneDistance: Single, farPlaneDistance: Single) -> Matrix4x4
        
            Creates a perspective projection matrix based on a field of view, aspect ratio, and near and far view plane distances.
        
            fieldOfView: The field of view in the y direction, in radians.
            aspectRatio: The aspect ratio, defined as view space width divided by height.
            nearPlaneDistance: The distance to the near view plane.
            farPlaneDistance: The distance to the far view plane.
            Returns: The perspective projection matrix.
        """
        pass

    @staticmethod
    def CreatePerspectiveOffCenter(left, right, bottom, top, nearPlaneDistance, farPlaneDistance):
        """
        CreatePerspectiveOffCenter(left: Single, right: Single, bottom: Single, top: Single, nearPlaneDistance: Single, farPlaneDistance: Single) -> Matrix4x4
        
            Creates a customized perspective projection matrix.
        
            left: The minimum x-value of the view volume at the near view plane.
            right: The maximum x-value of the view volume at the near view plane.
            bottom: The minimum y-value of the view volume at the near view plane.
            top: The maximum y-value of the view volume at the near view plane.
            nearPlaneDistance: The distance to the near view plane.
            farPlaneDistance: The distance to the far view plane.
            Returns: The perspective projection matrix.
        """
        pass

    @staticmethod
    def CreateReflection(value):
        """
        CreateReflection(value: Plane) -> Matrix4x4
        
            Creates a matrix that reflects the coordinate system about a specified plane.
        
            value: The plane about which to create a reflection.
            Returns: A new matrix expressing the reflection.
        """
        pass

    @staticmethod
    def CreateRotationX(radians, centerPoint=None):
        """
        CreateRotationX(radians: Single) -> Matrix4x4
        
            Creates a matrix for rotating points around the X axis.
        
            radians: The amount, in radians, by which to rotate around the X axis.
            Returns: The rotation matrix.
        CreateRotationX(radians: Single, centerPoint: Vector3) -> Matrix4x4
        
            Creates a matrix for rotating points around the X axis from a center point.
        
            radians: The amount, in radians, by which to rotate around the X axis.
            centerPoint: The center point.
            Returns: The rotation matrix.
        """
        pass

    @staticmethod
    def CreateRotationY(radians, centerPoint=None):
        """
        CreateRotationY(radians: Single) -> Matrix4x4
        
            Creates a matrix for rotating points around the Y axis.
        
            radians: The amount, in radians, by which to rotate around the Y-axis.
            Returns: The rotation matrix.
        CreateRotationY(radians: Single, centerPoint: Vector3) -> Matrix4x4
        
            The amount, in radians, by which to rotate around the Y axis from a center point.
        
            radians: The amount, in radians, by which to rotate around the Y-axis.
            centerPoint: The center point.
            Returns: The rotation matrix.
        """
        pass

    @staticmethod
    def CreateRotationZ(radians, centerPoint=None):
        """
        CreateRotationZ(radians: Single) -> Matrix4x4
        
            Creates a matrix for rotating points around the Z axis.
        
            radians: The amount, in radians, by which to rotate around the Z-axis.
            Returns: The rotation matrix.
        CreateRotationZ(radians: Single, centerPoint: Vector3) -> Matrix4x4
        
            Creates a matrix for rotating points around the Z axis from a center point.
        
            radians: The amount, in radians, by which to rotate around the Z-axis.
            centerPoint: The center point.
            Returns: The rotation matrix.
        """
        pass

    @staticmethod
    def CreateScale(*__args):
        """
        CreateScale(xScale: Single, yScale: Single, zScale: Single) -> Matrix4x4
        
            Creates a scaling matrix from the specified X, Y, and Z components.
        
            xScale: The value to scale by on the X axis.
            yScale: The value to scale by on the Y axis.
            zScale: The value to scale by on the Z axis.
            Returns: The scaling matrix.
        CreateScale(xScale: Single, yScale: Single, zScale: Single, centerPoint: Vector3) -> Matrix4x4
        
            Creates a scaling matrix that is offset by a given center point.
        
            xScale: The value to scale by on the X axis.
            yScale: The value to scale by on the Y axis.
            zScale: The value to scale by on the Z axis.
            centerPoint: The center point.
            Returns: The scaling matrix.
        CreateScale(scales: Vector3) -> Matrix4x4
        
            Creates a scaling matrix from the specified vector scale.
        
            scales: The scale to use.
            Returns: The scaling matrix.
        CreateScale(scales: Vector3, centerPoint: Vector3) -> Matrix4x4
        
            Creates a scaling matrix with a center point.
        
            scales: The vector that contains the amount to scale on each axis.
            centerPoint: The center point.
            Returns: The scaling matrix.
        CreateScale(scale: Single) -> Matrix4x4
        
            Creates a uniform scaling matrix that scale equally on each axis.
        
            scale: The uniform scaling factor.
            Returns: The scaling matrix.
        CreateScale(scale: Single, centerPoint: Vector3) -> Matrix4x4
        
            Creates a uniform scaling matrix that scales equally on each axis with a center point.
        
            scale: The uniform scaling factor.
            centerPoint: The center point.
            Returns: The scaling matrix.
        """
        pass

    @staticmethod
    def CreateShadow(lightDirection, plane):
        """
        CreateShadow(lightDirection: Vector3, plane: Plane) -> Matrix4x4
        
            Creates a matrix that flattens geometry into a specified plane as if casting a shadow from a specified light source.
        
            lightDirection: The direction from which the light that will cast the shadow is coming.
            plane: The plane onto which the new matrix should flatten geometry so as to cast a shadow.
            Returns: A new matrix that can be used to flatten geometry onto the specified plane from the specified direction.
        """
        pass

    @staticmethod
    def CreateTranslation(*__args):
        """
        CreateTranslation(position: Vector3) -> Matrix4x4
        
            Creates a translation matrix from the specified 3-dimensional vector.
        
            position: The amount to translate in each axis.
            Returns: The translation matrix.
        CreateTranslation(xPosition: Single, yPosition: Single, zPosition: Single) -> Matrix4x4
        
            Creates a translation matrix from the specified X, Y, and Z components.
        
            xPosition: The amount to translate on the X axis.
            yPosition: The amount to translate on the Y axis.
            zPosition: The amount to translate on the Z axis.
            Returns: The translation matrix.
        """
        pass

    @staticmethod
    def CreateWorld(position, forward, up):
        """
        CreateWorld(position: Vector3, forward: Vector3, up: Vector3) -> Matrix4x4
        
            Creates a world matrix with the specified parameters.
        
            position: The position of the object.
            forward: The forward direction of the object.
            up: The upward direction of the object. Its value is usually [0, 1, 0].
            Returns: The world matrix.
        """
        pass

    @staticmethod
    def Decompose(matrix, scale, rotation, translation):
        """
        Decompose(matrix: Matrix4x4) -> (bool, Vector3, Quaternion, Vector3)
        
            Attempts to extract the scale, translation, and rotation components from the given scale, rotation, or translation matrix. The return value indicates whether the operation succeeded.
        
            matrix: The source matrix.
            Returns: true if matrixmatrix was decomposed successfully; otherwise,  false.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Matrix4x4, other: Matrix4x4) -> bool
        
            Returns a value that indicates whether this instance and another 4x4 matrix are equal.
        
            other: The other matrix.
            Returns: true if the two matrices are equal; otherwise, false.
        Equals(self: Matrix4x4, obj: object) -> bool
        
            Returns a value that indicates whether this instance and a specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: true if the current instance and objobj are equal; otherwise, false. If objobj is null, the method returns false.
        """
        pass

    def GetDeterminant(self):
        """
        GetDeterminant(self: Matrix4x4) -> Single
        
            Calculates the determinant of the current 4x4 matrix.
            Returns: The determinant.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Matrix4x4) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code.
        """
        pass

    @staticmethod
    def Invert(matrix, result):
        """
        Invert(matrix: Matrix4x4) -> (bool, Matrix4x4)
        
            Inverts the specified matrix. The return value indicates whether the operation succeeded.
        
            matrix: The matrix to invert.
            Returns: true if matrixmatrix was converted successfully; otherwise,  false.
        """
        pass

    @staticmethod
    def Lerp(matrix1, matrix2, amount):
        """
        Lerp(matrix1: Matrix4x4, matrix2: Matrix4x4, amount: Single) -> Matrix4x4
        
            Performs a linear interpolation from one matrix to a second matrix based on a value that specifies the weighting of the second matrix.
        
            matrix1: The first matrix.
            matrix2: The second matrix.
            amount: The relative weighting of matrix2.
            Returns: The interpolated matrix.
        """
        pass

    @staticmethod
    def Multiply(value1, value2):
        """
        Multiply(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4
        
            Returns the matrix that results from multiplying two matrices together.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The product matrix.
        Multiply(value1: Matrix4x4, value2: Single) -> Matrix4x4
        
            Returns the matrix that results from scaling all the elements of a specified matrix by a scalar factor.
        
            value1: The matrix to scale.
            value2: The scaling value to use.
            Returns: The scaled matrix.
        """
        pass

    @staticmethod
    def Negate(value):
        """
        Negate(value: Matrix4x4) -> Matrix4x4
        
            Negates the specified matrix by multiplying all its values by -1.
        
            value: The matrix to negate.
            Returns: The negated matrix.
        """
        pass

    @staticmethod
    def Subtract(value1, value2):
        """
        Subtract(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4
        
            Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix containing the values that result from subtracting each element in value2value2 from its corresponding element in value1value1.
        """
        pass

    def ToString(self):
        """
        ToString(self: Matrix4x4) -> str
        
            Returns a string that represents this matrix.
            Returns: The string representation of this matrix.
        """
        pass

    @staticmethod
    def Transform(value, rotation):
        """
        Transform(value: Matrix4x4, rotation: Quaternion) -> Matrix4x4
        
            Transforms the specified matrix by applying the specified Quaternion rotation.
        
            value: The matrix to transform.
            rotation: The rotation t apply.
            Returns: The transformed matrix.
        """
        pass

    @staticmethod
    def Transpose(matrix):
        """
        Transpose(matrix: Matrix4x4) -> Matrix4x4
        
            Transposes the rows and columns of a matrix.
        
            matrix: The matrix to transpose.
            Returns: The transposed matrix.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, m11: Single, m12: Single, m13: Single, m14: Single, m21: Single, m22: Single, m23: Single, m24: Single, m31: Single, m32: Single, m33: Single, m34: Single, m41: Single, m42: Single, m43: Single, m44: Single)
        __new__(cls: type, value: Matrix3x2)
        __new__[Matrix4x4]() -> Matrix4x4
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4
        
            Adds each element in one matrix with its corresponding element in a second matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix that contains the summed values.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4
        
            Returns the matrix that results from multiplying two matrices together.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The product matrix.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(value1: Matrix4x4, value2: Matrix4x4) -> Matrix4x4
        
            Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
            value1: The first matrix.
            value2: The second matrix.
            Returns: The matrix containing the values that result from subtracting each element in value2value2 from its corresponding element in value1value1.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether the current matrix is the identity matrix.

Get: IsIdentity(self: Matrix4x4) -> bool

"""

    Translation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the translation component of this matrix.

Get: Translation(self: Matrix4x4) -> Vector3

Set: Translation(self: Matrix4x4) = value
"""


    Identity = None
    M11 = None
    M12 = None
    M13 = None
    M14 = None
    M21 = None
    M22 = None
    M23 = None
    M24 = None
    M31 = None
    M32 = None
    M33 = None
    M34 = None
    M41 = None
    M42 = None
    M43 = None
    M44 = None


class Plane(object, IEquatable[Plane]):
    """
    Represents a three-dimensional plane.
    
    Plane(x: Single, y: Single, z: Single, d: Single)
    Plane(normal: Vector3, d: Single)
    Plane(value: Vector4)
    """
    @staticmethod
    def CreateFromVertices(point1, point2, point3):
        """
        CreateFromVertices(point1: Vector3, point2: Vector3, point3: Vector3) -> Plane
        
            Creates a System.Numerics.Plane object that contains three specified points.
        
            point1: The first point defining the plane.
            point2: The second point defining the plane.
            point3: The third point defining the plane.
            Returns: The plane containing the three points.
        """
        pass

    @staticmethod
    def Dot(plane, value):
        """
        Dot(plane: Plane, value: Vector4) -> Single
        
            Calculates the dot product of a plane and a 4-dimensional vector.
        
            plane: The plane.
            value: The four-dimensional vector.
            Returns: The dot product.
        """
        pass

    @staticmethod
    def DotCoordinate(plane, value):
        """
        DotCoordinate(plane: Plane, value: Vector3) -> Single
        
            Returns the dot product of a specified three-dimensional vector and the normal vector of this plane plus the distance (System.Numerics.Plane.D) value of the plane.
        
            plane: The plane.
            value: The 3-dimensional vector.
            Returns: The dot product.
        """
        pass

    @staticmethod
    def DotNormal(plane, value):
        """
        DotNormal(plane: Plane, value: Vector3) -> Single
        
            Returns the dot product of a specified three-dimensional vector and the System.Numerics.Plane.Normal vector of this plane.
        
            plane: The plane.
            value: The three-dimensional vector.
            Returns: The dot product.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Plane, other: Plane) -> bool
        
            Returns a value that indicates whether this instance and another plane object are equal.
        
            other: The other plane.
            Returns: true if the two planes are equal; otherwise, false.
        Equals(self: Plane, obj: object) -> bool
        
            Returns a value that indicates whether this instance and a specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: true if the current instance and objobj are equal; otherwise, false. If objobj is null, the method returns false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Plane) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code.
        """
        pass

    @staticmethod
    def Normalize(value):
        """
        Normalize(value: Plane) -> Plane
        
            Creates a new System.Numerics.Plane object whose normal vector is the source plane&#39;s normal vector normalized.
        
            value: The source plane.
            Returns: The normalized plane.
        """
        pass

    def ToString(self):
        """
        ToString(self: Plane) -> str
        
            Returns the string representation of this plane object.
            Returns: A string that represents this stem.Numerics.Plane object.
        """
        pass

    @staticmethod
    def Transform(plane, *__args):
        """
        Transform(plane: Plane, matrix: Matrix4x4) -> Plane
        
            Transforms a normalized plane by a 4x4 matrix.
        
            plane: The normalized plane to transform.
            matrix: The transformation matrix to apply to plane.
            Returns: The transformed plane.
        Transform(plane: Plane, rotation: Quaternion) -> Plane
        
            Transforms a normalized plane by a Quaternion rotation.
        
            plane: The normalized plane to transform.
            rotation: The Quaternion rotation to apply to the plane.
            Returns: A new plane that results from applying the Quaternion rotation.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, x: Single, y: Single, z: Single, d: Single)
        __new__(cls: type, normal: Vector3, d: Single)
        __new__(cls: type, value: Vector4)
        __new__[Plane]() -> Plane
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    D = None
    Normal = None


class Quaternion(object, IEquatable[Quaternion]):
    """
    Represents a vector that is used to encode three-dimensional physical rotations.
    
    Quaternion(x: Single, y: Single, z: Single, w: Single)
    Quaternion(vectorPart: Vector3, scalarPart: Single)
    """
    @staticmethod
    def Add(value1, value2):
        """
        Add(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Adds each element in one quaternion with its corresponding element in a second quaternion.
        
            value1: The first quaternion.
            value2: The second quaternion.
            Returns: The quaternion that contains the summed values of value1value1 and value2value2.
        """
        pass

    @staticmethod
    def Concatenate(value1, value2):
        """
        Concatenate(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Concatenates two quaternions.
        
            value1: The first quaternion rotation in the series.
            value2: The second quaternion rotation in the series.
            Returns: A new quaternion representing the concatenation of the value1value1 rotation followed by the value2value2 rotation.
        """
        pass

    @staticmethod
    def Conjugate(value):
        """
        Conjugate(value: Quaternion) -> Quaternion
        
            Returns the conjugate of a specified quaternion.
        
            value: The quaternion.
            Returns: A new quaternion that is the conjugate of value.
        """
        pass

    @staticmethod
    def CreateFromAxisAngle(axis, angle):
        """
        CreateFromAxisAngle(axis: Vector3, angle: Single) -> Quaternion
        
            Creates a quaternion from a vector and an angle to rotate about the vector.
        
            axis: The vector to rotate around.
            angle: The angle, in radians, to rotate around the vector.
            Returns: The newly created quaternion.
        """
        pass

    @staticmethod
    def CreateFromRotationMatrix(matrix):
        """
        CreateFromRotationMatrix(matrix: Matrix4x4) -> Quaternion
        
            Creates a quaternion from the specified rotation matrix.
        
            matrix: The rotation matrix.
            Returns: The newly created quaternion.
        """
        pass

    @staticmethod
    def CreateFromYawPitchRoll(yaw, pitch, roll):
        """
        CreateFromYawPitchRoll(yaw: Single, pitch: Single, roll: Single) -> Quaternion
        
            Creates a new quaternion from the given yaw, pitch, and roll.
        
            yaw: The yaw angle, in radians, around the Y axis.
            pitch: The pitch angle, in radians, around the X axis.
            roll: The roll angle, in radians, around the Z axis.
            Returns: The resulting quaternion.
        """
        pass

    @staticmethod
    def Divide(value1, value2):
        """
        Divide(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Divides one quaternion by a second quaternion.
        
            value1: The dividend.
            value2: The divisor.
            Returns: The quaternion that results from dividing value1value1 by value2value2.
        """
        pass

    @staticmethod
    def Dot(quaternion1, quaternion2):
        """
        Dot(quaternion1: Quaternion, quaternion2: Quaternion) -> Single
        
            Calculates the dot product of two quaternions.
        
            quaternion1: The first quaternion.
            quaternion2: The second quaternion.
            Returns: The dot product.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Quaternion, other: Quaternion) -> bool
        
            Returns a value that indicates whether this instance and another quaternion are equal.
        
            other: The other quaternion.
            Returns: true if the two quaternions are equal; otherwise, false.
        Equals(self: Quaternion, obj: object) -> bool
        
            Returns a value that indicates whether this instance and a specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: true if the current instance and objobj are equal; otherwise, false. If objobj is null, the method returns false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Quaternion) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code.
        """
        pass

    @staticmethod
    def Inverse(value):
        """
        Inverse(value: Quaternion) -> Quaternion
        
            Returns the inverse of a quaternion.
        
            value: The quaternion.
            Returns: The inverted quaternion.
        """
        pass

    def Length(self):
        """
        Length(self: Quaternion) -> Single
        
            Calculates the length of the quaternion.
            Returns: The computed length of the quaternion.
        """
        pass

    def LengthSquared(self):
        """
        LengthSquared(self: Quaternion) -> Single
        
            Calculates the squared length of the quaternion.
            Returns: The length squared of the quaternion.
        """
        pass

    @staticmethod
    def Lerp(quaternion1, quaternion2, amount):
        """
        Lerp(quaternion1: Quaternion, quaternion2: Quaternion, amount: Single) -> Quaternion
        
            Performs a linear interpolation between two quaternions based on a value that specifies the weighting of the second quaternion.
        
            quaternion1: The first quaternion.
            quaternion2: The second quaternion.
            amount: The relative weight of quaternion2 in the interpolation.
            Returns: The interpolated quaternion.
        """
        pass

    @staticmethod
    def Multiply(value1, value2):
        """
        Multiply(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Returns the quaternion that results from multiplying two quaternions together.
        
            value1: The first quaternion.
            value2: The second quaternion.
            Returns: The product quaternion.
        Multiply(value1: Quaternion, value2: Single) -> Quaternion
        
            Returns the quaternion that results from scaling all the components of a specified quaternion by a scalar factor.
        
            value1: The source quaternion.
            value2: The scalar value.
            Returns: The scaled quaternion.
        """
        pass

    @staticmethod
    def Negate(value):
        """
        Negate(value: Quaternion) -> Quaternion
        
            Reverses the sign of each component of the quaternion.
        
            value: The quaternion to negate.
            Returns: The negated quaternion.
        """
        pass

    @staticmethod
    def Normalize(value):
        """
        Normalize(value: Quaternion) -> Quaternion
        
            Divides each component of a specified System.Numerics.Quaternion by its length.
        
            value: The quaternion to normalize.
            Returns: The normalized quaternion.
        """
        pass

    @staticmethod
    def Slerp(quaternion1, quaternion2, amount):
        """
        Slerp(quaternion1: Quaternion, quaternion2: Quaternion, amount: Single) -> Quaternion
        
            Interpolates between two quaternions, using spherical linear interpolation.
        
            quaternion1: The first quaternion.
            quaternion2: The second quaternion.
            amount: The relative weight of the second quaternion in the interpolation.
            Returns: The interpolated quaternion.
        """
        pass

    @staticmethod
    def Subtract(value1, value2):
        """
        Subtract(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Subtracts each element in a second quaternion from its corresponding element in a first quaternion.
        
            value1: The first quaternion.
            value2: The second quaternion.
            Returns: The quaternion containing the values that result from subtracting each element in value2value2 from its corresponding element in value1value1.
        """
        pass

    def ToString(self):
        """
        ToString(self: Quaternion) -> str
        
            Returns a string that represents this quaternion.
            Returns: The string representation of this quaternion.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, x: Single, y: Single, z: Single, w: Single)
        __new__(cls: type, vectorPart: Vector3, scalarPart: Single)
        __new__[Quaternion]() -> Quaternion
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Adds each element in one quaternion with its corresponding element in a second quaternion.
        
            value1: The first quaternion.
            value2: The second quaternion.
            Returns: The quaternion that contains the summed values of value1value1 and value2value2.
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Divides one quaternion by a second quaternion.
        
            value1: The dividend.
            value2: The divisor.
            Returns: The quaternion that results from dividing value1value1 by value2value2.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Returns the quaternion that results from multiplying two quaternions together.
        
            value1: The first quaternion.
            value2: The second quaternion.
            Returns: The product quaternion.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(value1: Quaternion, value2: Quaternion) -> Quaternion
        
            Subtracts each element in a second quaternion from its corresponding element in a first quaternion.
        
            value1: The first quaternion.
            value2: The second quaternion.
            Returns: The quaternion containing the values that result from subtracting each element in value2value2 from its corresponding element in value1value1.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether the current instance is the identity quaternion.

Get: IsIdentity(self: Quaternion) -> bool

"""


    Identity = None
    W = None
    X = None
    Y = None
    Z = None


class Vector2(object, IEquatable[Vector2], IFormattable):
    """
    Represents a vector with two single-precision floating-point values.
    
    Vector2(value: Single)
    Vector2(x: Single, y: Single)
    """
    @staticmethod
    def Abs(value):
        """
        Abs(value: Vector2) -> Vector2
        
            Returns a vector whose elements are the absolute values of each of the specified vector&#39;s elements.
        
            value: A vector.
            Returns: The absolute value vector.
        """
        pass

    @staticmethod
    def Add(left, right):
        """
        Add(left: Vector2, right: Vector2) -> Vector2
        
            Adds two vectors together.
        
            left: The first vector to add.
            right: The second vector to add.
            Returns: The summed vector.
        """
        pass

    @staticmethod
    def Clamp(value1, min, max):
        """
        Clamp(value1: Vector2, min: Vector2, max: Vector2) -> Vector2
        
            Restricts a vector between a minimum and a maximum value.
        
            value1: The vector to restrict.
            min: The minimum value.
            max: The maximum value.
            Returns: The restricted vector.
        """
        pass

    def CopyTo(self, array, index=None):
        """
        CopyTo(self: Vector2, array: Array[Single])
            Copies the elements of the vector to a specified array.
        
            array: The destination array.
        CopyTo(self: Vector2, array: Array[Single], index: int)
            Copies the elements of the vector to a specified array starting at a specified index position.
        
            array: The destination array.
            index: The index at which to copy the first element of the vector.
        """
        pass

    @staticmethod
    def Distance(value1, value2):
        """
        Distance(value1: Vector2, value2: Vector2) -> Single
        
            Computes the Euclidean distance between the two given points.
        
            value1: The first point.
            value2: The second point.
            Returns: The distance.
        """
        pass

    @staticmethod
    def DistanceSquared(value1, value2):
        """
        DistanceSquared(value1: Vector2, value2: Vector2) -> Single
        
            Returns the Euclidean distance squared between two specified points.
        
            value1: The first point.
            value2: The second point.
            Returns: The distance squared.
        """
        pass

    @staticmethod
    def Divide(left, *__args):
        """
        Divide(left: Vector2, right: Vector2) -> Vector2
        
            Divides the first vector by the second.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector resulting from the division.
        Divide(left: Vector2, divisor: Single) -> Vector2
        
            Divides the specified vector by a specified scalar value.
        
            left: The vector.
            divisor: The scalar value.
            Returns: The vector that results from the division.
        """
        pass

    @staticmethod
    def Dot(value1, value2):
        """
        Dot(value1: Vector2, value2: Vector2) -> Single
        
            Returns the dot product of two vectors.
        
            value1: The first vector.
            value2: The second vector.
            Returns: The dot product.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector2, obj: object) -> bool
        
            Returns a value that indicates whether this instance and a specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: true if the current instance and objobj are equal; otherwise, false. If objobj is null, the method returns false.
        Equals(self: Vector2, other: Vector2) -> bool
        
            Returns a value that indicates whether this instance and another vector are equal.
        
            other: The other vector.
            Returns: true if the two vectors are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Vector2) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code.
        """
        pass

    def Length(self):
        """
        Length(self: Vector2) -> Single
        
            Returns the length of the vector.
            Returns: The vector&#39;s length.
        """
        pass

    def LengthSquared(self):
        """
        LengthSquared(self: Vector2) -> Single
        
            Returns the length of the vector squared.
            Returns: The vector&#39;s length squared.
        """
        pass

    @staticmethod
    def Lerp(value1, value2, amount):
        """
        Lerp(value1: Vector2, value2: Vector2, amount: Single) -> Vector2
        
            Performs a linear interpolation between two vectors based on the given weighting.
        
            value1: The first vector.
            value2: The second vector.
            amount: A value between 0 and 1 that indicates the weight of value2.
            Returns: The interpolated vector.
        """
        pass

    @staticmethod
    def Max(value1, value2):
        """
        Max(value1: Vector2, value2: Vector2) -> Vector2
        
            Returns a vector whose elements are the maximum of each of the pairs of elements in two specified vectors.
        
            value1: The first vector.
            value2: The second vector.
            Returns: The maximized vector.
        """
        pass

    @staticmethod
    def Min(value1, value2):
        """
        Min(value1: Vector2, value2: Vector2) -> Vector2
        
            Returns a vector whose elements are the minimum of each of the pairs of elements in two specified vectors.
        
            value1: The first vector.
            value2: The second vector.
            Returns: The minimized vector.
        """
        pass

    @staticmethod
    def Multiply(left, right):
        """
        Multiply(left: Vector2, right: Vector2) -> Vector2
        
            Multiplies two vectors together.
        
            left: The first vector.
            right: The second vector.
            Returns: The product vector.
        Multiply(left: Vector2, right: Single) -> Vector2
        
            Multiplies a vector by a specified scalar.
        
            left: The vector to multiply.
            right: The scalar value.
            Returns: The scaled vector.
        Multiply(left: Single, right: Vector2) -> Vector2
        
            Multiplies a scalar value by a specified vector.
        
            left: The scaled value.
            right: The vector.
            Returns: The scaled vector.
        """
        pass

    @staticmethod
    def Negate(value):
        """
        Negate(value: Vector2) -> Vector2
        
            Negates a specified vector.
        
            value: The vector to negate.
            Returns: The negated vector.
        """
        pass

    @staticmethod
    def Normalize(value):
        """
        Normalize(value: Vector2) -> Vector2
        
            Returns a vector with the same direction as the specified vector, but with a length of one.
        
            value: The vector to normalize.
            Returns: The normalized vector.
        """
        pass

    @staticmethod
    def Reflect(vector, normal):
        """
        Reflect(vector: Vector2, normal: Vector2) -> Vector2
        
            Returns the reflection of a vector off a surface that has the specified normal.
        
            vector: The source vector.
            normal: The normal of the surface being reflected off.
            Returns: The reflected vector.
        """
        pass

    @staticmethod
    def SquareRoot(value):
        """
        SquareRoot(value: Vector2) -> Vector2
        
            Returns a vector whose elements are the square root of each of a specified vector&#39;s elements.
        
            value: A vector.
            Returns: The square root vector.
        """
        pass

    @staticmethod
    def Subtract(left, right):
        """
        Subtract(left: Vector2, right: Vector2) -> Vector2
        
            Subtracts the second vector from the first.
        
            left: The first vector.
            right: The second vector.
            Returns: The difference vector.
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: Vector2) -> str
        
            Returns the string representation of the current instance using default formatting.
            Returns: The string representation of the current instance.
        ToString(self: Vector2, format: str) -> str
        
            Returns the string representation of the current instance using the specified format string to format individual elements.
        
            format: A  or  that defines the format of individual elements.
            Returns: The string representation of the current instance.
        ToString(self: Vector2, format: str, formatProvider: IFormatProvider) -> str
        
            Returns the string representation of the current instance using the specified format string to format individual elements and the specified format provider to define culture-specific 
             formatting.
        
        
            format: A  or  that defines the format of individual elements.
            formatProvider: A format provider that supplies culture-specific formatting information.
            Returns: The string representation of the current instance.
        """
        pass

    @staticmethod
    def Transform(*__args):
        """
        Transform(position: Vector2, matrix: Matrix3x2) -> Vector2
        
            Transforms a vector by a specified 3x2 matrix.
        
            position: The vector to transform.
            matrix: The transformation matrix.
            Returns: The transformed vector.
        Transform(position: Vector2, matrix: Matrix4x4) -> Vector2
        
            Transforms a vector by a specified 4x4 matrix.
        
            position: The vector to transform.
            matrix: The transformation matrix.
            Returns: The transformed vector.
        Transform(value: Vector2, rotation: Quaternion) -> Vector2
        
            Transforms a vector by the specified Quaternion rotation value.
        
            value: The vector to rotate.
            rotation: The rotation to apply.
            Returns: The transformed vector.
        """
        pass

    @staticmethod
    def TransformNormal(normal, matrix):
        """
        TransformNormal(normal: Vector2, matrix: Matrix3x2) -> Vector2
        
            Transforms a vector normal by the given 3x2 matrix.
        
            normal: The source vector.
            matrix: The matrix.
            Returns: The transformed vector.
        TransformNormal(normal: Vector2, matrix: Matrix4x4) -> Vector2
        
            Transforms a vector normal by the given 4x4 matrix.
        
            normal: The source vector.
            matrix: The matrix.
            Returns: The transformed vector.
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, value: Single)
        __new__(cls: type, x: Single, y: Single)
        __new__[Vector2]() -> Vector2
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(left: Vector2, right: Vector2) -> Vector2
        
            Adds two vectors together.
        
            left: The first vector to add.
            right: The second vector to add.
            Returns: The summed vector.
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(left: Vector2, right: Vector2) -> Vector2
        
            Divides the first vector by the second.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector that results from dividing leftleft by rightright.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(left: Vector2, right: Vector2) -> Vector2
        
            Multiplies two vectors together.
        
            left: The first vector.
            right: The second vector.
            Returns: The product vector.
        __rmul__(left: Single, right: Vector2) -> Vector2
        
            Multiples the scalar value by the specified vector.
        
            left: The vector.
            right: The scalar value.
            Returns: The scaled vector.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(left: Vector2, right: Vector2) -> Vector2
        
            Subtracts the second vector from the first.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector that results from subtracting rightright from leftleft.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    One = None
    UnitX = None
    UnitY = None
    X = None
    Y = None
    Zero = None


class Vector3(object, IEquatable[Vector3], IFormattable):
    """
    Represents a vector with three  single-precision floating-point values.
    
    Vector3(value: Single)
    Vector3(value: Vector2, z: Single)
    Vector3(x: Single, y: Single, z: Single)
    """
    @staticmethod
    def Abs(value):
        """
        Abs(value: Vector3) -> Vector3
        
            Returns a vector whose elements are the absolute values of each of the specified vector&#39;s elements.
        
            value: A vector.
            Returns: The absolute value vector.
        """
        pass

    @staticmethod
    def Add(left, right):
        """
        Add(left: Vector3, right: Vector3) -> Vector3
        
            Adds two vectors together.
        
            left: The first vector to add.
            right: The second vector to add.
            Returns: The summed vector.
        """
        pass

    @staticmethod
    def Clamp(value1, min, max):
        """
        Clamp(value1: Vector3, min: Vector3, max: Vector3) -> Vector3
        
            Restricts a vector between a minimum and a maximum value.
        
            value1: The vector to restrict.
            min: The minimum value.
            max: The maximum value.
            Returns: The restricted vector.
        """
        pass

    def CopyTo(self, array, index=None):
        """
        CopyTo(self: Vector3, array: Array[Single])
            Copies the elements of the vector to a specified array.
        
            array: The destination array.
        CopyTo(self: Vector3, array: Array[Single], index: int)
            Copies the elements of the vector to a specified array starting at a specified index position.
        
            array: The destination array.
            index: The index at which to copy the first element of the vector.
        """
        pass

    @staticmethod
    def Cross(vector1, vector2):
        """
        Cross(vector1: Vector3, vector2: Vector3) -> Vector3
        
            Computes the cross product of two vectors.
        
            vector1: The first vector.
            vector2: The second vector.
            Returns: The cross product.
        """
        pass

    @staticmethod
    def Distance(value1, value2):
        """
        Distance(value1: Vector3, value2: Vector3) -> Single
        
            Computes the Euclidean distance between the two given points.
        
            value1: The first point.
            value2: The second point.
            Returns: The distance.
        """
        pass

    @staticmethod
    def DistanceSquared(value1, value2):
        """
        DistanceSquared(value1: Vector3, value2: Vector3) -> Single
        
            Returns the Euclidean distance squared between two specified points.
        
            value1: The first point.
            value2: The second point.
            Returns: The distance squared.
        """
        pass

    @staticmethod
    def Divide(left, *__args):
        """
        Divide(left: Vector3, right: Vector3) -> Vector3
        
            Divides the first vector by the second.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector resulting from the division.
        Divide(left: Vector3, divisor: Single) -> Vector3
        
            Divides the specified vector by a specified scalar value.
        
            left: The vector.
            divisor: The scalar value.
            Returns: The vector that results from the division.
        """
        pass

    @staticmethod
    def Dot(vector1, vector2):
        """
        Dot(vector1: Vector3, vector2: Vector3) -> Single
        
            Returns the dot product of two vectors.
        
            vector1: The first vector.
            vector2: The second vector.
            Returns: The dot product.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector3, obj: object) -> bool
        
            Returns a value that indicates whether this instance and a specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: true if the current instance and objobj are equal; otherwise, false. If objobj is null, the method returns false.
        Equals(self: Vector3, other: Vector3) -> bool
        
            Returns a value that indicates whether this instance and another vector are equal.
        
            other: The other vector.
            Returns: true if the two vectors are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Vector3) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code.
        """
        pass

    def Length(self):
        """
        Length(self: Vector3) -> Single
        
            Returns the length of this vector object.
            Returns: The vector&#39;s length.
        """
        pass

    def LengthSquared(self):
        """
        LengthSquared(self: Vector3) -> Single
        
            Returns the length of the vector squared.
            Returns: The vector&#39;s length squared.
        """
        pass

    @staticmethod
    def Lerp(value1, value2, amount):
        """
        Lerp(value1: Vector3, value2: Vector3, amount: Single) -> Vector3
        
            Performs a linear interpolation between two vectors based on the given weighting.
        
            value1: The first vector.
            value2: The second vector.
            amount: A value between 0 and 1 that indicates the weight of value2.
            Returns: The interpolated vector.
        """
        pass

    @staticmethod
    def Max(value1, value2):
        """
        Max(value1: Vector3, value2: Vector3) -> Vector3
        
            Returns a vector whose elements are the maximum of each of the pairs of elements in two specified vectors.
        
            value1: The first vector.
            value2: The second vector.
            Returns: The maximized vector.
        """
        pass

    @staticmethod
    def Min(value1, value2):
        """
        Min(value1: Vector3, value2: Vector3) -> Vector3
        
            Returns a vector whose elements are the minimum of each of the pairs of elements in two specified vectors.
        
            value1: The first vector.
            value2: The second vector.
            Returns: The minimized vector.
        """
        pass

    @staticmethod
    def Multiply(left, right):
        """
        Multiply(left: Vector3, right: Vector3) -> Vector3
        
            Multiplies two vectors together.
        
            left: The first vector.
            right: The second vector.
            Returns: The product vector.
        Multiply(left: Vector3, right: Single) -> Vector3
        
            Multiplies a vector by a specified scalar.
        
            left: The vector to multiply.
            right: The scalar value.
            Returns: The scaled vector.
        Multiply(left: Single, right: Vector3) -> Vector3
        
            Multiplies a scalar value by a specified vector.
        
            left: The scaled value.
            right: The vector.
            Returns: The scaled vector.
        """
        pass

    @staticmethod
    def Negate(value):
        """
        Negate(value: Vector3) -> Vector3
        
            Negates a specified vector.
        
            value: The vector to negate.
            Returns: The negated vector.
        """
        pass

    @staticmethod
    def Normalize(value):
        """
        Normalize(value: Vector3) -> Vector3
        
            Returns a vector with the same direction as the specified vector, but with a length of one.
        
            value: The vector to normalize.
            Returns: The normalized vector.
        """
        pass

    @staticmethod
    def Reflect(vector, normal):
        """
        Reflect(vector: Vector3, normal: Vector3) -> Vector3
        
            Returns the reflection of a vector off a surface that has the specified normal.
        
            vector: The source vector.
            normal: The normal of the surface being reflected off.
            Returns: The reflected vector.
        """
        pass

    @staticmethod
    def SquareRoot(value):
        """
        SquareRoot(value: Vector3) -> Vector3
        
            Returns a vector whose elements are the square root of each of a specified vector&#39;s elements.
        
            value: A vector.
            Returns: The square root vector.
        """
        pass

    @staticmethod
    def Subtract(left, right):
        """
        Subtract(left: Vector3, right: Vector3) -> Vector3
        
            Subtracts the second vector from the first.
        
            left: The first vector.
            right: The second vector.
            Returns: The difference vector.
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: Vector3) -> str
        
            Returns the string representation of the current instance using default formatting.
            Returns: The string representation of the current instance.
        ToString(self: Vector3, format: str) -> str
        
            Returns the string representation of the current instance using the specified format string to format individual elements.
        
            format: A  or  that defines the format of individual elements.
            Returns: The string representation of the current instance.
        ToString(self: Vector3, format: str, formatProvider: IFormatProvider) -> str
        
            Returns the string representation of the current instance using the specified format string to format individual elements and the specified format provider to define culture-specific 
             formatting.
        
        
            format: A  or  that defines the format of individual elements.
            formatProvider: A format provider that supplies culture-specific formatting information.
            Returns: The string representation of the current instance.
        """
        pass

    @staticmethod
    def Transform(*__args):
        """
        Transform(position: Vector3, matrix: Matrix4x4) -> Vector3
        
            Transforms a vector by a specified 4x4 matrix.
        
            position: The vector to transform.
            matrix: The transformation matrix.
            Returns: The transformed vector.
        Transform(value: Vector3, rotation: Quaternion) -> Vector3
        
            Transforms a vector by the specified Quaternion rotation value.
        
            value: The vector to rotate.
            rotation: The rotation to apply.
            Returns: The transformed vector.
        """
        pass

    @staticmethod
    def TransformNormal(normal, matrix):
        """
        TransformNormal(normal: Vector3, matrix: Matrix4x4) -> Vector3
        
            Transforms a vector normal by the given 4x4 matrix.
        
            normal: The source vector.
            matrix: The matrix.
            Returns: The transformed vector.
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, value: Single)
        __new__(cls: type, value: Vector2, z: Single)
        __new__(cls: type, x: Single, y: Single, z: Single)
        __new__[Vector3]() -> Vector3
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(left: Vector3, right: Vector3) -> Vector3
        
            Adds two vectors together.
        
            left: The first vector to add.
            right: The second vector to add.
            Returns: The summed vector.
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(left: Vector3, right: Vector3) -> Vector3
        
            Divides the first vector by the second.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector that results from dividing leftleft by rightright.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(left: Vector3, right: Vector3) -> Vector3
        
            Multiplies two vectors together.
        
            left: The first vector.
            right: The second vector.
            Returns: The product vector.
        __rmul__(left: Single, right: Vector3) -> Vector3
        
            Multiples the scalar value by the specified vector.
        
            left: The vector.
            right: The scalar value.
            Returns: The scaled vector.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(left: Vector3, right: Vector3) -> Vector3
        
            Subtracts the second vector from the first.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector that results from subtracting rightright from leftleft.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    One = None
    UnitX = None
    UnitY = None
    UnitZ = None
    X = None
    Y = None
    Z = None
    Zero = None


class Vector4(object, IEquatable[Vector4], IFormattable):
    """
    Represents a vector with four single-precision floating-point values.
    
    Vector4(value: Single)
    Vector4(x: Single, y: Single, z: Single, w: Single)
    Vector4(value: Vector2, z: Single, w: Single)
    Vector4(value: Vector3, w: Single)
    """
    @staticmethod
    def Abs(value):
        """
        Abs(value: Vector4) -> Vector4
        
            Returns a vector whose elements are the absolute values of each of the specified vector&#39;s elements.
        
            value: A vector.
            Returns: The absolute value vector.
        """
        pass

    @staticmethod
    def Add(left, right):
        """
        Add(left: Vector4, right: Vector4) -> Vector4
        
            Adds two vectors together.
        
            left: The first vector to add.
            right: The second vector to add.
            Returns: The summed vector.
        """
        pass

    @staticmethod
    def Clamp(value1, min, max):
        """
        Clamp(value1: Vector4, min: Vector4, max: Vector4) -> Vector4
        
            Restricts a vector between a minimum and a maximum value.
        
            value1: The vector to restrict.
            min: The minimum value.
            max: The maximum value.
            Returns: The restricted vector.
        """
        pass

    def CopyTo(self, array, index=None):
        """
        CopyTo(self: Vector4, array: Array[Single])
            Copies the elements of the vector to a specified array.
        
            array: The destination array.
        CopyTo(self: Vector4, array: Array[Single], index: int)
            Copies the elements of the vector to a specified array starting at a specified index position.
        
            array: The destination array.
            index: The index at which to copy the first element of the vector.
        """
        pass

    @staticmethod
    def Distance(value1, value2):
        """
        Distance(value1: Vector4, value2: Vector4) -> Single
        
            Computes the Euclidean distance between the two given points.
        
            value1: The first point.
            value2: The second point.
            Returns: The distance.
        """
        pass

    @staticmethod
    def DistanceSquared(value1, value2):
        """
        DistanceSquared(value1: Vector4, value2: Vector4) -> Single
        
            Returns the Euclidean distance squared between two specified points.
        
            value1: The first point.
            value2: The second point.
            Returns: The distance squared.
        """
        pass

    @staticmethod
    def Divide(left, *__args):
        """
        Divide(left: Vector4, right: Vector4) -> Vector4
        
            Divides the first vector by the second.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector resulting from the division.
        Divide(left: Vector4, divisor: Single) -> Vector4
        
            Divides the specified vector by a specified scalar value.
        
            left: The vector.
            divisor: The scalar value.
            Returns: The vector that results from the division.
        """
        pass

    @staticmethod
    def Dot(vector1, vector2):
        """
        Dot(vector1: Vector4, vector2: Vector4) -> Single
        
            Returns the dot product of two vectors.
        
            vector1: The first vector.
            vector2: The second vector.
            Returns: The dot product.
        """
        pass

    def Equals(self, *__args):
        """
        Equals(self: Vector4, obj: object) -> bool
        
            Returns a value that indicates whether this instance and a specified object are equal.
        
            obj: The object to compare with the current instance.
            Returns: true if the current instance and objobj are equal; otherwise, false. If objobj is null, the method returns false.
        Equals(self: Vector4, other: Vector4) -> bool
        
            Returns a value that indicates whether this instance and another vector are equal.
        
            other: The other vector.
            Returns: true if the two vectors are equal; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: Vector4) -> int
        
            Returns the hash code for this instance.
            Returns: The hash code.
        """
        pass

    def Length(self):
        """
        Length(self: Vector4) -> Single
        
            Returns the length of this vector object.
            Returns: The vector&#39;s length.
        """
        pass

    def LengthSquared(self):
        """
        LengthSquared(self: Vector4) -> Single
        
            Returns the length of the vector squared.
            Returns: The vector&#39;s length squared.
        """
        pass

    @staticmethod
    def Lerp(value1, value2, amount):
        """
        Lerp(value1: Vector4, value2: Vector4, amount: Single) -> Vector4
        
            Performs a linear interpolation between two vectors based on the given weighting.
        
            value1: The first vector.
            value2: The second vector.
            amount: A value between 0 and 1 that indicates the weight of value2.
            Returns: The interpolated vector.
        """
        pass

    @staticmethod
    def Max(value1, value2):
        """
        Max(value1: Vector4, value2: Vector4) -> Vector4
        
            Returns a vector whose elements are the maximum of each of the pairs of elements in two specified vectors.
        
            value1: The first vector.
            value2: The second vector.
            Returns: The maximized vector.
        """
        pass

    @staticmethod
    def Min(value1, value2):
        """
        Min(value1: Vector4, value2: Vector4) -> Vector4
        
            Returns a vector whose elements are the minimum of each of the pairs of elements in two specified vectors.
        
            value1: The first vector.
            value2: The second vector.
            Returns: The minimized vector.
        """
        pass

    @staticmethod
    def Multiply(left, right):
        """
        Multiply(left: Vector4, right: Vector4) -> Vector4
        
            Multiplies two vectors together.
        
            left: The first vector.
            right: The second vector.
            Returns: The product vector.
        Multiply(left: Vector4, right: Single) -> Vector4
        
            Multiplies a vector by a specified scalar.
        
            left: The vector to multiply.
            right: The scalar value.
            Returns: The scaled vector.
        Multiply(left: Single, right: Vector4) -> Vector4
        
            Multiplies a scalar value by a specified vector.
        
            left: The scaled value.
            right: The vector.
            Returns: The scaled vector.
        """
        pass

    @staticmethod
    def Negate(value):
        """
        Negate(value: Vector4) -> Vector4
        
            Negates a specified vector.
        
            value: The vector to negate.
            Returns: The negated vector.
        """
        pass

    @staticmethod
    def Normalize(vector):
        """
        Normalize(vector: Vector4) -> Vector4
        
            Returns a vector with the same direction as the specified vector, but with a length of one.
        
            vector: The vector to normalize.
            Returns: The normalized vector.
        """
        pass

    @staticmethod
    def SquareRoot(value):
        """
        SquareRoot(value: Vector4) -> Vector4
        
            Returns a vector whose elements are the square root of each of a specified vector&#39;s elements.
        
            value: A vector.
            Returns: The square root vector.
        """
        pass

    @staticmethod
    def Subtract(left, right):
        """
        Subtract(left: Vector4, right: Vector4) -> Vector4
        
            Subtracts the second vector from the first.
        
            left: The first vector.
            right: The second vector.
            Returns: The difference vector.
        """
        pass

    def ToString(self, format=None, formatProvider=None):
        """
        ToString(self: Vector4) -> str
        
            Returns the string representation of the current instance using default formatting.
            Returns: The string representation of the current instance.
        ToString(self: Vector4, format: str) -> str
        
            Returns the string representation of the current instance using the specified format string to format individual elements.
        
            format: A  or  that defines the format of individual elements.
            Returns: The string representation of the current instance.
        ToString(self: Vector4, format: str, formatProvider: IFormatProvider) -> str
        
            Returns the string representation of the current instance using the specified format string to format individual elements and the specified format provider to define culture-specific 
             formatting.
        
        
            format: A  or  that defines the format of individual elements.
            formatProvider: A format provider that supplies culture-specific formatting information.
            Returns: The string representation of the current instance.
        """
        pass

    @staticmethod
    def Transform(*__args):
        """
        Transform(position: Vector2, matrix: Matrix4x4) -> Vector4
        
            Transforms a two-dimensional vector by a specified 4x4 matrix.
        
            position: The vector to transform.
            matrix: The transformation matrix.
            Returns: The transformed vector.
        Transform(position: Vector3, matrix: Matrix4x4) -> Vector4
        
            Transforms a three-dimensional vector by a specified 4x4 matrix.
        
            position: The vector to transform.
            matrix: The transformation matrix.
            Returns: The transformed vector.
        Transform(vector: Vector4, matrix: Matrix4x4) -> Vector4
        
            Transforms a four-dimensional vector by a specified 4x4 matrix.
        
            vector: The vector to transform.
            matrix: The transformation matrix.
            Returns: The transformed vector.
        Transform(value: Vector2, rotation: Quaternion) -> Vector4
        
            Transforms a two-dimensional vector by the specified Quaternion rotation value.
        
            value: The vector to rotate.
            rotation: The rotation to apply.
            Returns: The transformed vector.
        Transform(value: Vector3, rotation: Quaternion) -> Vector4
        
            Transforms a three-dimensional vector by the specified Quaternion rotation value.
        
            value: The vector to rotate.
            rotation: The rotation to apply.
            Returns: The transformed vector.
        Transform(value: Vector4, rotation: Quaternion) -> Vector4
        
            Transforms a four-dimensional vector by the specified Quaternion rotation value.
        
            value: The vector to rotate.
            rotation: The rotation to apply.
            Returns: The transformed vector.
        """
        pass

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, value: Single)
        __new__(cls: type, x: Single, y: Single, z: Single, w: Single)
        __new__(cls: type, value: Vector2, z: Single, w: Single)
        __new__(cls: type, value: Vector3, w: Single)
        __new__[Vector4]() -> Vector4
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(left: Vector4, right: Vector4) -> Vector4
        
            Adds two vectors together.
        
            left: The first vector to add.
            right: The second vector to add.
            Returns: The summed vector.
        """
        pass

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(left: Vector4, right: Vector4) -> Vector4
        
            Divides the first vector by the second.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector that results from dividing leftleft by rightright.
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(left: Vector4, right: Vector4) -> Vector4
        
            Multiplies two vectors together.
        
            left: The first vector.
            right: The second vector.
            Returns: The product vector.
        __rmul__(left: Single, right: Vector4) -> Vector4
        
            Multiples the scalar value by the specified vector.
        
            left: The vector.
            right: The scalar value.
            Returns: The scaled vector.
        """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(left: Vector4, right: Vector4) -> Vector4
        
            Subtracts the second vector from the first.
        
            left: The first vector.
            right: The second vector.
            Returns: The vector that results from subtracting rightright from leftleft.
        """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        pass

    One = None
    UnitW = None
    UnitX = None
    UnitY = None
    UnitZ = None
    W = None
    X = None
    Y = None
    Z = None
    Zero = None


