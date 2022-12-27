DO $$
	DECLARE
		brands_id brands.brand_id%TYPE;
		brands_name brands.brand_name%TYPE;
		
	BEGIN
		brands_id := 4;
		brands_name := 'brand';
		FOR counter IN 1..5
			LOOP
				INSERT INTO brands (brand_id, brand_name)
				VALUES (counter + brands_id, brands_name || counter + brands_id);
			END LOOP;
	END;
$$